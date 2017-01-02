//import * as R from 'ramda';

export const SET_ENV_NAME = 'SET_ENV_NAME';

export function setEnvName(envName) {
  return {
    type: SET_ENV_NAME,
    payload: {
      envName: envName
    }
  };
}
