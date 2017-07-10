###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.events.event_port_update import EventPortUpdate
from test.event_based_scan.test_data.event_payload_port_update import EVENT_PAYLOAD_PORT_UPDATE, PORT_DOCUMENT
from test.event_based_scan.test_event import TestEvent


class TestPortUpdate(TestEvent):

    def test_handle_port_update(self):
        self.values = EVENT_PAYLOAD_PORT_UPDATE
        self.payload = self.values['payload']
        self.port = self.payload['port']
        self.port_id = self.port['id']

        # set port data firstly.
        self.inv.set(PORT_DOCUMENT)

        # add network document
        EventPortUpdate().handle(self.env, self.values)

        # check network document
        port_document = self.inv.get_by_id(self.env, self.port_id)
        self.assertIsNotNone(port_document)
        self.assertEqual(port_document["name"], self.port['name'])
        self.assertEqual(port_document['admin_state_up'], self.port['admin_state_up'])
        self.assertEqual(port_document['binding:vnic_type'], self.port['binding:vnic_type'])
