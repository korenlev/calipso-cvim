import { combineReducers } from 'redux';

import { navigation } from './navigation';

const osdnaApp = combineReducers({
  api: combineReducers({
    navigation: navigation,
  })
});

export default osdnaApp;
