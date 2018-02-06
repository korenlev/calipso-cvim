from discover.events.event_base import EventResult
from discover.events.kube.kube_event_base import KubeEventBase
from discover.events.kube.kube_pod_update import KubePodUpdate


class KubePodAdd(KubeEventBase):

    def handle(self, env, values):
        super().handle(env, values)

        pod = self.inv.get_by_id(environment=env, item_id=self.object_id)
        if pod:
            return EventResult(result=False,
                               retry=False,
                               related_object=self.object_id,
                               display_context=self.object_id,
                               message='Pod already exists')

        self.inv.set(self.prepare_pod_doc())
        return EventResult(result=True,
                           related_object=self.object_id,
                           display_context=self.object_id)