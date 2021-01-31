###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Union, List


class DefaultDistTranslator:
    DOCKER_CALL = 'docker exec --user root'

    # To be defined in subclasses
    TRANSLATIONS_PER_MECHANISM_DRIVER = {
        "ALL": {},
        "VPP": {},
        "OVS": {}
    }

    def __init__(self, mechanism_drivers: List[str], distribution_version: str):
        self.mechanism_drivers = [md.upper() for md in mechanism_drivers]
        self.distribution_version = distribution_version
        self.translations = self.TRANSLATIONS_PER_MECHANISM_DRIVER.get("ALL", {})
        for mechanism_driver in self.mechanism_drivers:
            self.translations.update(self.TRANSLATIONS_PER_MECHANISM_DRIVER.get(mechanism_driver, {}))

    def render_template(self, command_to_translate: str,
                        translation_key: str, translation_template: str) -> str:
        translation_dict = {
            'docker_call': self.DOCKER_CALL,
            'version': self.distribution_version,
            'cmd': translation_key
        }
        translated_command = translation_template.format(**translation_dict)
        translated_command = command_to_translate.replace(translation_key, translated_command)
        return translated_command

    def translate(self, cmd: str) -> str:
        for translation_key, translation_template in self.translations.items():
            if translation_key in cmd:
                return self.render_template(command_to_translate=cmd,
                                            translation_key=translation_key,
                                            translation_template=translation_template)
        return cmd


class MercuryDistTranslator(DefaultDistTranslator):
    TRANSLATIONS_PER_MECHANISM_DRIVER = {
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
    }

    MIN_RHEL8_VERSION = 27747
    RHEL8_DOCKER_EXEC_CMD = "docker exec --user root --workdir /root"

    def __init__(self, mechanism_drivers: List[str], distribution_version: str):
        super().__init__(mechanism_drivers=mechanism_drivers, distribution_version=distribution_version)
        try:
            dv_int = int(self.distribution_version)
            if dv_int >= self.MIN_RHEL8_VERSION:
                self.DOCKER_CALL = self.RHEL8_DOCKER_EXEC_CMD
        except ValueError:
            # Invalid (non-integer) distribution version
            pass


class KollaDistTranslator(DefaultDistTranslator):
    TRANSLATIONS_PER_MECHANISM_DRIVER = {
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


class CliDistTranslator:
    MERCURY_DISTRIBUTION = "MERCURY"
    KOLLA_DISTRIBUTION = "KOLLA"

    TRANSLATOR_CLASSES = {
        "MERCURY": MercuryDistTranslator,
        "KOLLA": KollaDistTranslator
    }

    def __init__(self, env: dict):
        self.translator: DefaultDistTranslator = self.get_translator(
            mechanism_drivers=env['mechanism_drivers'],
            distribution=env['distribution'],
            distribution_version=env['distribution_version']
        )

    @classmethod
    def get_translator(cls, mechanism_drivers: Union[List[str], str],
                       distribution: str, distribution_version: str) -> DefaultDistTranslator:

        distribution = distribution.upper()
        if isinstance(mechanism_drivers, str):
            mechanism_drivers = [mechanism_drivers]

        translator_cls = cls.TRANSLATOR_CLASSES.get(distribution, DefaultDistTranslator)
        return translator_cls(
            mechanism_drivers=mechanism_drivers,
            distribution_version=distribution_version
        )

    def translate(self, command_to_translate: str) -> str:
        return self.translator.translate(cmd=command_to_translate)
