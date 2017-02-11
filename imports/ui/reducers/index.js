import { combineReducers } from 'redux';

import { navigation } from './navigation';
import { searchInterestedParties } from './search-interested-parties';
import { reducer as environmentPanel } from './environment-panel.reducer';
import { reducer as i18n } from './i18n.reducer';
import { reducer as graphTooltipWindow } from './graph-tooltip-window.reducer';
import { reducer as vedgeInfoWindow } from './vedge-info-window.reducer';

const osdnaApp = combineReducers({
  api: combineReducers({
    navigation,
    searchInterestedParties,
    i18n
  }),
  components: combineReducers({
    environmentPanel,
    graphTooltipWindow,
    vedgeInfoWindow
  })
});

export default osdnaApp;
