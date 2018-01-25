from discover.events.kube.kube_event_base import KubeEventBase


class KubePodDelete(KubeEventBase):

    def handle(self, env, values):
        super().handle(env, values)
        print("Event: Pod delete. "
              "Namespace: {ns}. "
              "Pod name: {pn}".format(ns=self.metadata.namespace,
                                      pn=self.metadata.name))
