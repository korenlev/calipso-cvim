from discover.events.event_delete_base import EventDeleteBase
from discover.events.kube.kube_event_base import KubeEventBase


class KubeEventDeleteBase(KubeEventBase, EventDeleteBase):
    pass
