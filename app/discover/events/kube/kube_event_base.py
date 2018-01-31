from kubernetes.client import V1Pod

from discover.events.event_base import EventBase
from discover.fetchers.kube.kube_fetch_pods import KubeFetchPods


class KubeEventBase(EventBase):

    def __init__(self):
        super().__init__()
        self.object = None
        self.object_id = None
        self.metadata = None

    def handle(self, env, values):
        self.setup(env=env)
        self.object = values['object']
        self.metadata = self.object.metadata
        self.object_id = self.metadata.uid

        self.log.debug("Event: {type}. "
                       "Namespace: {namespace}. "
                       "Object name: {obj_name}, uid: {uid}"
                       .format(type="{} {}".format(values['object'].kind,
                                                   values['type']),
                               namespace=self.metadata.namespace,
                               obj_name=self.metadata.name,
                               uid=self.object_id))

    def prepare_pod_doc(self, pod: V1Pod = None):
        if not pod:
            pod = self.object

        host_id = pod.spec.node_name  # TODO: is this correct?
        host_name = pod.spec.node_name  # TODO: is this correct?

        doc = KubeFetchPods.get_pod_details(pod)
        self.set_folder_parent(doc, object_type='pod',
                               master_parent_type='host',
                               master_parent_id=host_id)
        doc['type'] = 'pod'
        doc['environment'] = self.env
        doc['host'] = host_name
        doc['name_path'] = "/".join(("", host_name,
                                     "Hosts", host_name,
                                     "Pods", doc['name']))
        doc['id_path'] = "/".join(("", host_id,
                                   "{}-hosts".format(host_id), host_id,
                                   "{}-pods".format(host_id), doc['name']))
        doc['show_in_tree'] = True
        return doc
