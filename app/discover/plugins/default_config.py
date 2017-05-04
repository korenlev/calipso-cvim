handlers_package = 'discover.events'

queues = [{'queue': 'notifications.nova', 'exchange': 'nova'},
          {'queue': 'notifications.neutron', 'exchange': 'neutron'},
          {'queue': 'notifications.neutron', 'exchange': 'dhcp_agent'},
          {'queue': 'notifications.info', 'exchange': 'info'}]

event_handlers = {'compute.instance.create.end': 'EventInstanceAdd',
                  'compute.instance.rebuild.end': 'EventInstanceAdd',
                  'compute.instance.update': 'EventInstanceUpdate',
                  'compute.instance.delete.end': 'EventInstanceDelete',

                  'network.create.start': 'EventNetworkAdd',
                  'network.create.end': 'EventNetworkAdd',
                  'network.update': 'EventNetworkUpdate',
                  'network.update.start': 'EventNetworkUpdate',
                  'network.update.end': 'EventNetworkUpdate',
                  'network.delete': 'EventNetworkDelete',
                  'network.delete.start': 'EventNetworkDelete',
                  'network.delete.end': 'EventNetworkDelete',

                  'subnet.create': 'EventSubnetAdd',
                  'subnet.create.start': 'EventSubnetAdd',
                  'subnet.create.end': 'EventSubnetAdd',
                  'subnet.update': 'EventSubnetUpdate',
                  'subnet.update.start': 'EventSubnetUpdate',
                  'subnet.update.end': 'EventSubnetUpdate',
                  'subnet.delete': 'EventSubnetDelete',
                  'subnet.delete.start': 'EventSubnetDelete',
                  'subnet.delete.end': 'EventSubnetDelete',

                  'port.create.end': 'EventPortAdd',
                  'port.update.end': 'EventPortUpdate',
                  'port.delete.end': 'EventPortDelete',

                  'router.create': 'EventRouterAdd',
                  'router.create.start': 'EventRouterAdd',
                  'router.create.end': 'EventRouterAdd',
                  'router.update': 'EventRouterUpdate',
                  'router.update.start': 'EventRouterUpdate',
                  'router.update.end': 'EventRouterUpdate',
                  'router.delete': 'EventRouterDelete',
                  'router.delete.start': 'EventRouterDelete',
                  'router.delete.end': 'EventRouterDelete',

                  'router.interface.create': 'EventInterfaceAdd',
                  'router.interface.delete': 'EventInterfaceDelete'}
