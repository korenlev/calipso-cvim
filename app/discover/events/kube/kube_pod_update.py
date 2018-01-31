from discover.events.event_base import EventResult
from discover.events.kube.kube_event_base import KubeEventBase


class KubePodUpdate(KubeEventBase):

    def handle(self, env, values):
        super().handle(env, values)

        pod = self.inv.get_by_id(environment=env, item_id=self.object_id)
        if not pod:
            return EventResult(result=False,
                               retry=True,  # TODO: doesn't work atm
                               related_object=self.object_id,
                               display_context=self.object_id,
                               message='Pod doesn\'t exist')

        self.inv.set(self.prepare_pod_doc())
        return EventResult(result=True,
                           related_object=self.object_id,
                           display_context=self.object_id)