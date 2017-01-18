//import * as R from 'ramda';

const defaultState = { 
  apis: {

  },
  collections: {
    environments: {
      fields: {
        eventBasedScan: {
          label: 'Event based scan',
          desc: 'Update the inventory in real-time whenever a user makes a change to the OpenStack environment'
        }
      }
    }
  },
  components: {
  }
};

export function reducer(state = defaultState, action) {
  switch (action.type) {

  default: 
    return state;
  }
}
