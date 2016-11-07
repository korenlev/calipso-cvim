import { combineReducers } from 'redux';

import { navigation } from './navigation';
import { searchInterestedParties } from './search-interested-parties';

const osdnaApp = combineReducers({
  api: combineReducers({
    navigation,
    searchInterestedParties,
  })
});

export default osdnaApp;
