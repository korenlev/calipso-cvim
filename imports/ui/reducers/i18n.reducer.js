//import * as R from 'ramda';

const defaultState = { 
  apis: {

  },
  collections: {
    environments: {
      fields: {
        eventBasedScan: {
          header: 'Event based scan',
          desc: 'Update the inventory in real-time whenever a user makes a change to the OpenStack environment'
        }
      }
    }
  },
  components: {
    environment: {
      briefInfos: {
        lastScanning: {
          header: 'Last scanning'
        },
        vConnectorsNum: {
          header: 'Number of vConnectors'
        },
        hostsNum: {
          header: 'Number of hosts'
        },
        vServicesNum: {
          header: 'Number of vServices'
        },
        instancesNum: {
          header: 'Number of instances'
        }
      }
    },
    projectDashboard: {
      infoBoxes: {
        networks: {
          header: 'Number of networks'
        },
        ports: {
          header: 'Number of ports'
        }
      }
    }
  }
};

export function reducer(state = defaultState, action) {
  switch (action.type) {

  default: 
    return state;
  }
}
