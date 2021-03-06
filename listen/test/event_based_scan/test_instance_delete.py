###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from listen.events.event_instance_delete import EventInstanceDelete
from listen.test.event_based_scan.test_data.event_payload_instance_delete \
    import EVENT_PAYLOAD_INSTANCE_DELETE, INSTANCE_DOCUMENT
from listen.test.event_based_scan.test_event_delete_base import TestEventDeleteBase


class TestInstanceDelete(TestEventDeleteBase):

    def setUp(self):
        super().setUp()
        self.values = EVENT_PAYLOAD_INSTANCE_DELETE

    def test_handle_instance_delete(self):
        self.handle_delete(handler=EventInstanceDelete(),
                           db_object=INSTANCE_DOCUMENT)
