import { combineReducers } from 'redux';

import navigation from './navigation';

const osdnaApp = combineReducers({
  api: combineReducers({
    navigation,
  })
});

export default osdnaApp;
