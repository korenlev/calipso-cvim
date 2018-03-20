from test.fetch.kube_fetch.test_data.kube_access import HOST_DOC

HOST_DOC = HOST_DOC.copy()
HOST_DOC['annotations'] = {
    "node.alpha.kubernetes.io/ttl": "0",
    "flannel.alpha.coreos.com/backend-data": "{\"VtepMAC\":\"be:9b:77:4d:31:9c\"}",
    "flannel.alpha.coreos.com/backend-type": "vxlan",
    "volumes.kubernetes.io/controller-managed-attach-detach": "true",
    "flannel.alpha.coreos.com/public-ip": "172.16.100.2",
    "flannel.alpha.coreos.com/kube-subnet-manager": "true"
}

OTEPS_FOLDER_ID = '{}-oteps'.format(HOST_DOC['id'])
