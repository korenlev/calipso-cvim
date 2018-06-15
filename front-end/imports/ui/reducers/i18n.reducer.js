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
      noGraphForLeafMsg: 'No clique for this focal_point',
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
        },
        containersNum: {
            header: 'Number of containers'
        },
        podsNum: {
            header: 'Number of pods'
        },
      },
      newBriefInfos: {
        lastScanning: {
          header: 'Last scanning'
        },
        vConnectorsNum: {
          header: 'vConnectors'
        },
        hostsNum: {
          header: 'Hosts'
        },
        vServicesNum: {
          header: 'vServices'
        },
        instancesNum: {
          header: 'Instances'
        },
        containersNum: {
            header: 'Containers'
        },
        podsNum: {
            header: 'Pods'
        },
      },
      newListInfoBoxes: {
        regions: {
          header: 'Regions',
          baseType: 'region'
        },
        projects: {
          header: 'Projects',
          baseType: 'project'
        },
        networks: {
          header: 'Networks',
          baseType: 'network'
        },
        hosts: {
          header: 'Hosts',
          baseType: 'host'
        }
      },
      listInfoBoxes: {
        regions: {
          header: 'Regions'
        },
        projects: {
          header: 'Projects'
        },
        networks: {
          header: 'Networks'
        },
        hosts: {
          header: 'Hosts'
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
    },

    regionDashboard: {
      infoBoxes: {
        instances: {
          header: 'Number of instances'
        },
        vServices: {
          header: 'Number of vServices'
        },
        hosts: {
          header: 'Number of hosts'
        },
        vConnectors: {
          header: 'Number of vConnectors'
        }
      },
      listInfoBoxes: {
        availabilityZones: {
          header: 'Availability zones'
        },
        aggregates: {
          header: 'Aggregates'
        }
      }
    },

    zoneDashboard: {
      infoBoxes: {
        instances: {
          header: 'Number of instances'
        },
        vServices: {
          header: 'Number of vServices'
        },
        hosts: {
          header: 'Number of hosts'
        },
        vConnectors: {
          header: 'Number of vConnectors'
        },
        vEdges: {
          header: 'Number of vEdges'
        }
      },
      listInfoBoxes: {
        hosts: {
          header: 'Hosts'
        },
      }
    },

    aggregateDashboard: {
      infoBoxes: {
        instances: {
          header: 'Number of instances'
        },
        vServices: {
          header: 'Number of vServices'
        },
        hosts: {
          header: 'Number of hosts'
        },
        vConnectors: {
          header: 'Number of vConnectors'
        },
        vEdges: {
          header: 'Number of vEdges'
        }
      },
      listInfoBoxes: {
        hosts: {
          header: 'Hosts'
        },
      }
    },

    hostDashboard: {
      infoBoxes: {
        instances: {
          header: 'Number of instances'
        },
        vServices: {
          header: 'Number of vServices'
        },
        vConnectors: {
          header: 'Number of vConnectors'
        },
        networkAgents: {
          header: 'Number of agents'
        },
        pnics: {
          header: 'Number of pnics'
        },
        vEdges: {
          header: 'Number of vEdges'
        },
        ports: {
          header: 'Number of ports'
        }
      },
    },

    generalFolderNodeDashboard: {
      mainCubic: {
        header: 'Number of children'
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
