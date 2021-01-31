###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Any

import kubernetes.client as kube_client

from base.utils.api_access_base import ApiAccessBase
from base.utils.kube_utils import update_resource_version
from base.utils.origins import Origin


class KubeAccess(ApiAccessBase):

    # TODO: make use of these fields (work out a reliable way to remove them from class attrs)
    EXTRA_FIELDS = ['attribute_map', 'swagger_types']

    def __init__(self, config=None):
        # Reset api client to support multiple configurations
        kube_client.configuration.api_client = None

        super().__init__('Kubernetes', config)

        self.base_url = None
        self.bearer_token = None
        self.api = None
        self.set_kube_config()

    def set_kube_config(self):
        self.base_url = 'https://{}:{}'.format(self.host, self.port)
        self.bearer_token = self.api_config.get('token', '')
        conf = kube_client.Configuration()
        conf.host = self.base_url
        conf.user = self.api_config.get('user')
        conf.api_key_prefix['authorization'] = 'Bearer'
        conf.api_key['authorization'] = self.bearer_token
        conf.verify_ssl = False
        self.api = kube_client.CoreV1Api(kube_client.ApiClient(conf))

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.set_kube_config()

    def update_resource_version(self, method: str,
                                resource_version):
        update_resource_version(inv=self.inv,
                                env=self.env,
                                method=method,
                                resource_version=resource_version)

    @classmethod
    def class_to_dict(cls, data_object: Any, include: list = None, exclude: list = None,
                      delete_extra_fields: bool = True) -> dict:
        """
            Convert a k8s data class to a dict.
            If an "include" list is supplied, only fields listed there are converted.
            Otherwise, all fields are converted excluding:
                - meta fields (starting with _),
                - non-callable fields (methods),
                - field listed in the "exclude" list argument,
        :param data_object: any class object
        :param include: list of fields to be converted from class object
        :param exclude: list of fields to be excluded from class object
        :return:
        """
        ret = {}
        if include is None:
            include = []
        if exclude is None:
            exclude = []

        attrs = [
            attr for attr in dir(data_object)
            # If include list is passed, just check it
            if (
                include and attr in include
            )
            or
            # If not, apply all exclusion rules
            (
                not include and attr not in exclude and not attr.startswith('_')
            )
        ]

        for attr in attrs:
            try:
                v = getattr(data_object, attr)
                if not callable(v):
                    if hasattr(v, "to_dict"):
                        v = v.to_dict()
                    ret[attr] = v
            except (TypeError, AttributeError):
                continue
        return ret
