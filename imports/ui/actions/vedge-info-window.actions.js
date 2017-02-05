//import * as R from 'ramda';

export const ACTIVATE_VEDGE_INFO_WINDOW = 'ACTIVATE_VEDGE_INFO_WINDOW';
export const CLOSE_VEDGE_INFO_WINDOW = 'CLOSE_VEDGE_INFO_WINDOW';

export function activateVedgeInfoWindow(node, left, top) {
  return {
    type: ACTIVATE_VEDGE_INFO_WINDOW,
    payload: {
      node: node,
      left: left,
      top: top
    }
  };
}

export function closeVedgeInfoWindow() {
  return {
    type: CLOSE_VEDGE_INFO_WINDOW
  };
}
