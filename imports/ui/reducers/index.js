import { combineReducers } from 'redux';

import { navigation } from './navigation';
import { searchInterestedParties } from './search-interested-parties';
import { reducer as environmentPanel } from './environment-panel.reducer';
import { reducer as i18n } from './i18n.reducer';

const osdnaApp = combineReducers({
  api: combineReducers({
    navigation,
    searchInterestedParties,
    i18n
  }),
  components: combineReducers({
    environmentPanel
  })
});

export default osdnaApp;
