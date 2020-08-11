###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################


class CliDistTranslator:

    DOCKER_CALL = 'docker exec --user root'

    MIN_RHEL8_VERSION = 27747

    TRANSLATIONS = {
        # special handling of cli commands in Mercury environments
        'Mercury': {
            'ALL': {
                'ip netns list': '{docker_call} neutron_l3_agent_{version} {cmd};;;'
                                 '{docker_call} neutron_dhcp_agent_{version} {cmd}',
                'ip netns exec qdhcp': '{docker_call} neutron_dhcp_agent_{version} {cmd}',
                'ip netns exec qrouter': '{docker_call} neutron_l3_agent_{version} {cmd}',
                'virsh': '{docker_call} novalibvirt_{version} {cmd}',
            },
            'VPP': {
                'ip -d link': '{docker_call} neutron_vpp_{version} {cmd}',
                'vppctl': '{docker_call} neutron_vpp_{version} {cmd}',
            },
            'OVS': {
                'ip link': '{docker_call} ovs_vswitch_{version} {cmd}',
                'ip -d link': '{docker_call} ovs_vswitch_{version} {cmd}',
                'bridge fdb show': '{docker_call} ovs_vswitch_{version} {cmd}',
                'brctl': '{docker_call} ovs_vswitch_{version} {cmd}',
                'ovs-vsctl': '{docker_call} ovs_vswitch_{version} {cmd}',
                'ovs-dpctl': '{docker_call} ovs_vswitch_{version} {cmd}',
            },
        },
        'Kolla': {
            'ALL': {
                'ip netns list': '{docker_call} neutron_l3_agent {cmd};;;'
                                 '{docker_call} neutron_dhcp_agent {cmd}',
                'ip netns exec qdhcp': '{docker_call} neutron_dhcp_agent {cmd}',
                'ip netns exec qrouter': '{docker_call} neutron_l3_agent {cmd}',
                'virsh': '{docker_call} nova_libvirt {cmd}',
            },
            'VPP': {
                'ip -d link': '{docker_call} neutron_vpp {cmd}',
                'vppctl': '{docker_call} neutron_vpp {cmd}',
            },
            'OVS': {
                'ip link': '{docker_call} openvswitch_vswitchd {cmd}',
                'ip -d link': '{docker_call} openvswitch_vswitchd {cmd}',
                'ovs-vsctl': '{docker_call} openvswitch_vswitchd {cmd}',
                'ovs-dpctl': '{docker_call} openvswitch_vswitchd {cmd}',
            },
        }
    }

    def __init__(self, env: dict):
        self.dist_version = env['distribution_version']
        # since RHEL8 and docker version 18.x we need to add a --workdir to docker exec commands
        # TODO rely on Docker version rather then mercury tag, but in any case this translations are done for mercury
        current_dist_version = int(self.dist_version)
        min_rhel8_dist_version = self.MIN_RHEL8_VERSION
        if current_dist_version >= min_rhel8_dist_version:
            self.DOCKER_CALL = 'docker exec --user root --workdir /root'
        self.translation = {}
        dist_translations = self.TRANSLATIONS.get(env['distribution'], {})
        if not dist_translations:
            return
        else:
            self.translation = dist_translations.get('ALL', {})
            for mechanism_driver in env['mechanism_drivers']:
                md_translations = dist_translations.get(mechanism_driver.upper(), {})
                if md_translations:
                    self.translation.update(md_translations)

    def translate(self, command_to_translate: str) -> str:
        for command in self.translation.keys():
            if command in command_to_translate:
                return self.command_translation(command_to_translate,
                                                command)
        return command_to_translate

    def command_translation(self, command_to_translate: str,
                            translation_key: str) -> str:
        cmd_translation = self.translation.get(translation_key)
        if not cmd_translation:
            return command_to_translate
        translation_dict = {
            'docker_call': self.DOCKER_CALL,
            'version': self.dist_version,
            'cmd': translation_key
        }
        cmd_translation = cmd_translation.format(**translation_dict)
        cmd_translation = command_to_translate.replace(translation_key,
                                                       cmd_translation)
        return cmd_translation
