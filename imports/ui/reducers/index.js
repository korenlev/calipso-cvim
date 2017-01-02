import { combineReducers } from 'redux';

import { navigation } from './navigation';
import { searchInterestedParties } from './search-interested-parties';
import { reducer as environmentPanel } from './environment-panel.reducer';

const osdnaApp = combineReducers({
  api: combineReducers({
    navigation,
    searchInterestedParties,
  }),
  components: combineReducers({
    environmentPanel
  })
});

export default osdnaApp;
