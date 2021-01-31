###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import logging
import os
import socket
from typing import Dict

import paramiko
from paramiko.buffered_pipe import PipeTimeout
from sshtunnel import SSHTunnelForwarder, BaseSSHTunnelForwarderError

from base.utils.configuration import Configuration
from base.utils.exceptions import CredentialsError, HostAddressError, SshError
from base.utils.logging.full_logger import FullLogger
from base.utils.logging.logger import Logger
from base.utils.singleton import Singleton
from base.utils.string_utils import binary2str


class MasterHostDetails:
    # TODO: sftp support?
    def __init__(self, host: str, user: str, port: int = 22, key: str = None, pwd: str = None):
        self.host: str = host
        self.port: int = port
        self.user: str = user
        self.key: str = key
        self.pwd: str = pwd
        self.check_host_details()

    @staticmethod
    def from_configuration(host_name: str = None) -> "MasterHostDetails":
        cli_conf = Configuration().get("CLI")
        if not cli_conf:
            raise ValueError("No CLI config in configuration")

        if 'hosts' in cli_conf:
            if not host_name:
                raise ValueError('MasterHostDetails: host must be specified if multi-host CLI config is used')
            if host_name not in cli_conf['hosts']:
                raise ValueError('MasterHostDetails: host details missing for host {}'.format(host_name))
            host_conf = cli_conf['hosts'][host_name]
        else:
            host_conf = cli_conf

        return MasterHostDetails(host=host_conf.get("host"), user=host_conf.get("user"),
                                 port=host_conf.get("port", 22), key=host_conf.get("key"),
                                 pwd=host_conf.get("pwd"))

    def check_host_details(self):
        if not self.host:
            raise ValueError('Missing definition of host for CLI access')
        if not self.user:
            raise ValueError('Missing definition of user for CLI access to host {}'.format(self.host))
        if self.key and not os.path.exists(self.key):
            raise ValueError('Key file not found: {}'.format(self.key))
        if not self.key and not self.pwd:
            raise ValueError('Must specify key or password for CLI access to host {}'.format(self.host))


class RemoteHostConnection:
    def __init__(self, host: str, ssh_tunnel: SSHTunnelForwarder, ssh_client: paramiko.SSHClient):
        self.host = host
        self.ssh_tunnel = ssh_tunnel
        self.ssh_client = ssh_client

    @property
    def is_connected(self) -> bool:
        return (
            self.ssh_tunnel and self.ssh_tunnel.is_active and self.ssh_client
        )  # TODO: check ssh client connection?

    def disconnect(self) -> None:
        self.ssh_tunnel.stop()
        self.ssh_client.close()


class SshTunnelConnection(metaclass=Singleton):
    LOG_NAME = "SshTunnelConnection"
    LOG_FILE = "ssh_tunnel_connection.log"
    LOG_LEVEL = Logger.INFO

    LOCAL_BIND_ADDRESS = "127.0.0.2"
    KEEP_ALIVE = 600
    REMOTE_TIMEOUT = 600
    SSH_CMD_TIMEOUT = 15

    # Remote host connections (hostname -> connection details)
    connections: Dict[str, RemoteHostConnection] = {}

    def __init__(self, master_host_details: MasterHostDetails):
        self.master_host_details: MasterHostDetails = master_host_details
        self.log: Logger = FullLogger(name=self.LOG_NAME, log_file=self.LOG_FILE, level=self.LOG_LEVEL)
        # silence paramiko logger
        logging.getLogger("paramiko").setLevel("CRITICAL")

    @classmethod
    def is_remote_host_connected(cls, host: str) -> bool:
        return host in cls.connections and cls.connections[host].is_connected

    def connect_ssh_tunnel(self, host: str) -> SSHTunnelForwarder:
        try:
            ssh_tunnel_logger = FullLogger(name="SSH Tunnel", log_file=self.LOG_FILE, level=Logger.ERROR)
            ssh_tunnel = SSHTunnelForwarder(
                ssh_address_or_host=(self.master_host_details.host, self.master_host_details.port),
                ssh_username=self.master_host_details.user,
                ssh_password=self.master_host_details.pwd if self.master_host_details.pwd else None,
                ssh_pkey=self.master_host_details.key if self.master_host_details.key else None,
                local_bind_address=(self.LOCAL_BIND_ADDRESS,),
                remote_bind_address=(host, 22),
                set_keepalive=self.KEEP_ALIVE,
                logger=ssh_tunnel_logger.log
            )
            ssh_tunnel.start()
            if not ssh_tunnel.is_active:
                raise SshError("Failed to setup SSH tunnel to remote host: {}".format(host))
        # TODO: verify exceptions
        except (SshError, BaseSSHTunnelForwarderError) as e:
            self.log.error("Error on SSH Tunnel: {}".format(e))
            msg = "Failed to setup tunnel to remote host: {}".format(host)
            raise HostAddressError(msg)
        self.log.info("SshTunnelConnection: ****** Connected SSH tunnel "
                      "from local address {}:{} to remote host: {}".format(ssh_tunnel.local_bind_host,
                                                                           ssh_tunnel.local_bind_port,
                                                                           host))
        return ssh_tunnel

    def connect_ssh_client(self, host: str, port: int = 22) -> paramiko.SSHClient:
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(username=self.master_host_details.user, key_filename=self.master_host_details.key,
                               hostname=self.LOCAL_BIND_ADDRESS, port=port, timeout=self.REMOTE_TIMEOUT)

        except paramiko.ssh_exception.AuthenticationException:
            msg = 'Failed authentication on SSH connect to host {}, port={}'.format(host, port)
            self.log.error(msg)
            raise CredentialsError(msg)
        except (paramiko.ssh_exception.SSHException, TimeoutError, PipeTimeout):
            msg = 'Timeout creating SSH connection to host {}, port={}'.format(host, port)
            self.log.error(msg)
            raise HostAddressError(msg)
        except Exception as e:
            msg = 'Failed to connect to host {} via SSH. Error: {}'.format(host, e)
            self.log.error(msg)
            raise HostAddressError(msg)
        self.log.info("SshTunnelConnection: ****** Connected SSH client to host: {}".format(host))
        return ssh_client

    def connect_to_remote_host(self, host: str, reconnect: bool = False) -> None:
        if self.is_remote_host_connected(host):
            if not reconnect:
                return
            self.connections[host].disconnect()

        ssh_tunnel = self.connect_ssh_tunnel(host=host)
        ssh_client = self.connect_ssh_client(host=host, port=ssh_tunnel.local_bind_port)
        self.connections[host] = RemoteHostConnection(host=host, ssh_tunnel=ssh_tunnel, ssh_client=ssh_client)

    @classmethod
    def disconnect_remote(cls, host: str) -> None:
        if cls.is_remote_host_connected(host):
            cls.connections[host].disconnect()
            del cls.connections[host]

    @classmethod
    def disconnect_all(cls):
        for connection in cls.connections.values():
            connection.disconnect()
        cls.connections = {}

    # @measure_perf_time(name="exec_on_host")
    def exec_on_host(self, cmd: str, host: str = None) -> str:
        if not host:
            host = self.master_host_details.host
        if not self.is_remote_host_connected(host):
            self.connect_to_remote_host(host=host)
        return self.exec(cmd=cmd, connection=self.connections[host])

    # @measure_perf_time(name="exec")
    def exec(self, cmd: str, connection: RemoteHostConnection) -> str:
        try:
            stdin, stdout, stderr = connection.ssh_client.exec_command(cmd, timeout=self.SSH_CMD_TIMEOUT)
        except (AttributeError, PipeTimeout, socket.timeout) as e:
            msg = 'Error when executing command: {}, error: {}'.format(cmd, e)
            self.log.error(msg)
            raise SshError(msg)

        try:
            try:
                err = binary2str(stderr.read())
            except (PipeTimeout, socket.timeout) as e:
                msg = 'Timeout when reading stderr from host {}, cmd={}: {}'.format(connection.host, cmd, e)
                self.log.error(msg)
                raise SshError(msg)

            if stdout.channel.recv_exit_status() != 0 and err:
                if err.splitlines():
                    msg = "CLI access: \nHost: {}\nCommand: {}\nError: {}\n".format(connection.host, cmd, err)
                    self.log.error(msg)
                    raise SshError(msg)

            try:
                ret = binary2str(stdout.read())
            except (PipeTimeout, socket.timeout) as e:
                msg = 'Timeout when reading stdout from host {}, cmd={}: {}'.format(connection.host, cmd, e)
                self.log.error(msg)
                raise SshError(msg)
        finally:
            stdin.close()
            stderr.close()
            stdout.close()

        return ret
