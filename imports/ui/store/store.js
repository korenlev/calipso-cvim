import { createStore } from 'redux';
import osdnaApp from '/imports/ui/reducers/index';

const store = createStore(osdnaApp);

export {
  store,
};
