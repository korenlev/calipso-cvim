import * as R from 'ramda';

import * as actions from '/imports/ui/actions/vedge-info-window.actions';

const defaultState = { 
  node: {},
  left: 0,
  top: 0,
  show: false
};

export function reducer(state = defaultState, action) {
  switch (action.type) {
  case actions.ACTIVATE_VEDGE_INFO_WINDOW:
    return R.merge(state, {
      node: R.pick(['_id', 'id', 'id_path', 'name', 'name_path'], action.payload.node),
      left: action.payload.left,
      top: action.payload.top - 28,
      show: true
    });

  case actions.CLOSE_VEDGE_INFO_WINDOW:
    return R.merge(state, {
      show: false,
      top: 0,
      left: 0
    });

  default: 
    return state;
  }
}
