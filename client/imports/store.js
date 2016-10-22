import { createStore } from 'redux';
import osdnaApp from '/client/imports/reducers/index';

const store = createStore(osdnaApp);

export {
  store,
};
