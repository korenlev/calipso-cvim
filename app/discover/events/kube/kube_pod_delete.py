from discover.events.kube.kube_event_delete_base import KubeEventDeleteBase


class KubePodDelete(KubeEventDeleteBase):

    def handle(self, env, values):
        super().handle(env, values)
        return self.delete_handler(env=env,
                                   object_id=self.object_id,
                                   object_type="pod")
