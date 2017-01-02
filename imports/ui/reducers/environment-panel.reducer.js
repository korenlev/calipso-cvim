import * as R from 'ramda';

import * as actions from '/imports/ui/actions/environment-panel.actions';

const defaultState = { 
  envName: null
};

export function reducer(state = defaultState, action) {
  switch (action.type) {
  case actions.SET_ENV_NAME:
    return R.assoc('envName', action.payload.envName, state);

  default: 
    return state;
  }
}
