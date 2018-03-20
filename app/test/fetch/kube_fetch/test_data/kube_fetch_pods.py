from test.fetch.kube_fetch.test_data.kube_access import BASE_RESPONSE

HOST_DOC = {
    "_id": "5aae890147d0b83dd2989dd7",
    "environment": "kube-aci",
    "id": "kub2-aci",
    "name": "kub2-aci",
    "name_path": "/kube-aci/Hosts/kub2-aci",
    "host": "kub2-aci",
    "uid": "6671a0b8-1b33-11e8-9d88-00505699cf9e",
    "parent_type": "hosts_folder",
    "parent_id": "kube-aci-hosts",
    "object_name": "kub2-aci",
    "id_path": "/kube-aci/kube-aci-hosts/kub2-aci"
}

NAMESPACE_DOC = {
    "_id": "5aae890147d0b83dd2989de3",
    "environment": "kube-aci",
    "id": "b5fee42e-1b31-11e8-9d88-00505699cf9e",
    "type": "namespace",
    "uid": "b5fee42e-1b31-11e8-9d88-00505699cf9e",
    "name": "default",
    "parent_type": "namespaces_folder",
    "name_path": "/kube-aci/Namespaces/default",
    "parent_id": "kube-aci-namespaces",
    "object_name": "default",
    "id_path": "/kube-aci/kube-aci-namespaces/b5fee42e-1b31-11e8-9d88-00505699cf9e",
    "pods": [
        {
            "name": "cisco-portal-deployment-ha-74f6b66557-wjpg2",
            "host": "kub2-aci",
            "id": "01df21c6-1b34-11e8-9d88-00505699cf9e"
        },
        {
            "name": "cisco-portal-deployment-ha-74f6b66557-2dc2x",
            "host": "kub3-aci",
            "id": "01de20a7-1b34-11e8-9d88-00505699cf9e"
        }
    ]
}

EMPTY_RESPONSE = BASE_RESPONSE.copy()
EMPTY_RESPONSE['kind'] = "PodList"
EMPTY_RESPONSE['metadata']['selfLink'] = "/api/v1/pods"

PODS_RESPONSE = EMPTY_RESPONSE.copy()
PODS_RESPONSE['items'] = [
    {
        "metadata": {
            "name": "cisco-portal-deployment-ha-74f6b66557-wjpg2",
            "generateName": "cisco-portal-deployment-ha-74f6b66557-",
            "namespace": "default",
            "selfLink": "/api/v1/namespaces/default/pods/cisco-portal-deployment-ha-74f6b66557-wjpg2",
            "uid": "01df21c6-1b34-11e8-9d88-00505699cf9e",
            "resourceVersion": "1921451",
            "creationTimestamp": "2018-02-26T20:31:21Z",
            "labels": {
                "app": "cisco-web",
                "pod-template-hash": "3092622113"
            },
        },
        "spec": {
            "containers": [
                {
                    "name": "cisco-web-portal",
                    "image": "korenlev/calipso:cisco-web",
                    "ports": [
                        {
                            "hostPort": 8008,
                            "containerPort": 22,
                            "protocol": "TCP"
                        }
                    ],
                    "resources": {},
                    "volumeMounts": [
                        {
                            "name": "default-token-l47rs",
                            "readOnly": True,
                            "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount"
                        }
                    ],
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File",
                    "imagePullPolicy": "IfNotPresent"
                }
            ],
            "restartPolicy": "Always",
            "terminationGracePeriodSeconds": 30,
            "dnsPolicy": "ClusterFirst",
            "serviceAccountName": "default",
            "serviceAccount": "default",
            "nodeName": "kub2-aci",
            "securityContext": {},
            "schedulerName": "default-scheduler",
        },
        "status": {
            "phase": "Running",
            "hostIP": "10.56.0.116",
            "podIP": "10.244.1.3",
            "startTime": "2018-02-26T20:31:22Z",
            "containerStatuses": [
                {
                    "name": "cisco-web-portal",
                    "state": {
                        "running": {
                            "startedAt": "2018-03-18T15:07:47Z"
                        }
                    },
                    "lastState": {
                        "terminated": {
                            "exitCode": 255,
                            "reason": "Error",
                            "startedAt": "2018-02-26T20:31:23Z",
                            "finishedAt": "2018-03-18T15:07:37Z",
                            "containerID": "docker://aa335750544c05fadd473dd841ff86111af4508311365e07391c5374e7e3c858"
                        }
                    },
                    "ready": True,
                    "restartCount": 1,
                    "image": "korenlev/calipso:cisco-web",
                    "imageID": "docker-pullable://korenlev/calipso@sha256:c877b2df87cc5f05c190c0e2473880d007408b0be421830d2fbd83c8f9e29b35",
                    "containerID": "docker://c6e22b9b79bd39309efbad6aa14a379e35b17379737a5a405d31f7186f327d83"
                }
            ],
            "qosClass": "BestEffort"
        }
    }
]
