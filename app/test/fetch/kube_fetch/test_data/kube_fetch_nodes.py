from test.fetch.kube_fetch.test_data.kube_access import BASE_RESPONSE

EMPTY_RESPONSE = BASE_RESPONSE.copy()
EMPTY_RESPONSE['kind'] = "NodeList"
EMPTY_RESPONSE['metadata']['selfLink'] = "/api/v1/nodes"

NODES_RESPONSE = EMPTY_RESPONSE.copy()
NODES_RESPONSE['items'] = [
    {
        "metadata": {
            "name": "kub1-aci",
            "selfLink": "/api/v1/nodes/kub1-aci",
            "uid": "b5fc42cf-1b31-11e8-9d88-00505699cf9e",
            "resourceVersion": "2022069",
            "creationTimestamp": "2018-02-26T20:14:55Z",
            "labels": {
                "beta.kubernetes.io/arch": "amd64",
                "beta.kubernetes.io/os": "linux",
                "kubernetes.io/hostname": "kub1-aci",
                "node-role.kubernetes.io/master": ""
            },
            "annotations": {
                "flannel.alpha.coreos.com/public-ip": "172.16.100.1",
            }
        },
        "spec": {
            "podCIDR": "10.244.0.0/24",
            "externalID": "kub1-aci"
        },
        "status": {
            "capacity": {
                "cpu": "2",
                "memory": "16432840Ki",
                "pods": "110"
            },
            "allocatable": {
                "cpu": "2",
                "memory": "16330440Ki",
                "pods": "110"
            },
            "addresses": [
                {
                    "type": "InternalIP",
                    "address": "10.56.0.117"
                },
                {
                    "type": "Hostname",
                    "address": "kub1-aci"
                }
            ],
            "daemonEndpoints": {
                "kubeletEndpoint": {
                    "Port": 10250
                }
            },
            "nodeInfo": {
                "machineID": "d1e524fa2d6b92a8a7fd55bc5a9419ab",
                "systemUUID": "4219C414-6073-9C04-43E9-FBEE1498A59A",
                "bootID": "f2f8a217-0282-478b-a0d2-7051c5369f50",
                "kernelVersion": "4.4.0-62-generic",
                "osImage": "Ubuntu 16.04.2 LTS",
                "containerRuntimeVersion": "docker://17.12.0-ce",
                "kubeletVersion": "v1.9.3",
                "kubeProxyVersion": "v1.9.3",
                "operatingSystem": "linux",
                "architecture": "amd64"
            },
        }
    },
    {
        "metadata": {
            "name": "kub2-aci",
            "selfLink": "/api/v1/nodes/kub2-aci",
            "uid": "6671a0b8-1b33-11e8-9d88-00505699cf9e",
            "resourceVersion": "2022063",
            "creationTimestamp": "2018-02-26T20:27:01Z",
            "labels": {
                "beta.kubernetes.io/arch": "amd64",
                "beta.kubernetes.io/os": "linux",
                "kubernetes.io/hostname": "kub2-aci"
            },
            "annotations": {
                "flannel.alpha.coreos.com/public-ip": "172.16.100.2"
            }
        },
        "spec": {
            "podCIDR": "10.244.1.0/24",
            "externalID": "kub2-aci"
        },
        "status": {
            "addresses": [
                {
                    "type": "InternalIP",
                    "address": "10.56.0.116"
                },
                {
                    "type": "Hostname",
                    "address": "kub2-aci"
                }
            ],
            "daemonEndpoints": {
                "kubeletEndpoint": {
                    "Port": 10250
                }
            },
            "nodeInfo": {
                "machineID": "d1e524fa2d6b92a8a7fd55bc5a9419ab",
                "systemUUID": "42198DD0-A393-9695-2207-C56505993966",
                "bootID": "4dc100cd-e646-48ed-9c91-df12025f9e1c",
                "kernelVersion": "4.4.0-62-generic",
                "osImage": "Ubuntu 16.04.2 LTS",
                "containerRuntimeVersion": "docker://17.12.0-ce",
                "kubeletVersion": "v1.9.3",
                "kubeProxyVersion": "v1.9.3",
                "operatingSystem": "linux",
                "architecture": "amd64"
            },
        }
    },
    {
        "metadata": {
            "name": "kub3-aci",
            "selfLink": "/api/v1/nodes/kub3-aci",
            "uid": "67dfe5f4-1b33-11e8-9d88-00505699cf9e",
            "resourceVersion": "2022068",
            "creationTimestamp": "2018-02-26T20:27:03Z",
            "labels": {
                "beta.kubernetes.io/arch": "amd64",
                "beta.kubernetes.io/os": "linux",
                "kubernetes.io/hostname": "kub3-aci"
            },
            "annotations": {
                "flannel.alpha.coreos.com/public-ip": "172.16.100.3"
            }
        },
        "spec": {
            "podCIDR": "10.244.2.0/24",
            "externalID": "kub3-aci"
        },
        "status": {
            "addresses": [
                {
                    "type": "InternalIP",
                    "address": "10.56.0.113"
                },
                {
                    "type": "Hostname",
                    "address": "kub3-aci"
                }
            ],
            "daemonEndpoints": {
                "kubeletEndpoint": {
                    "Port": 10250
                }
            },
            "nodeInfo": {
                "machineID": "d1e524fa2d6b92a8a7fd55bc5a9419ab",
                "systemUUID": "42193E70-A613-5A7B-20B8-7E71EDE2F164",
                "bootID": "dff71c30-e4b4-4336-9a7e-8689f8617f85",
                "kernelVersion": "4.4.0-62-generic",
                "osImage": "Ubuntu 16.04.2 LTS",
                "containerRuntimeVersion": "docker://17.12.0-ce",
                "kubeletVersion": "v1.9.3",
                "kubeProxyVersion": "v1.9.3",
                "operatingSystem": "linux",
                "architecture": "amd64"
            }
        }
    }
]
