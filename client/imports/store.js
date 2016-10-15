import { createStore } from 'redux';
import navigation from '/client/imports/reducers/navigation';

// Create global store for access in blaze components. Like collections.
let store = createStore(navigation);

export {
  store
};
