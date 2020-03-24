const { callApi } = require('../../services/restApi');
const { GET } = require('../../constants/apiMethods');
const { INVENTORY } = require('../../constants/apiPorts');

const getObjectTypes = async (endPoint) => {
  const { inventoryToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/constants?name=object_types`;
  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
};

const getEnvironmentConfigs = async (endPoint) => {
  const { inventoryToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/environment_configs`;
  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
};

const getInventoryList = async (endPoint, environment, type, projection) => {
  const { inventoryToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/inventory?env_name=${environment}&type=${type}&projection=${projection}`;
  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
};

const getInventoryItem = async (endPoint, environment, type, id, projection) => {
  const { inventoryToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/inventory?env_name=${environment}&type=${type}&id=${id}&projection=${projection}`;
  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
};

module.exports = {
  getEnvironmentConfigs,
  getObjectTypes,
  getInventoryList,
  getInventoryItem,
};
