const { callApi } = require('../../services/restApi');
const { GET } = require('../../constants/apiMethods');
const { INVENTORY } = require('../../constants/apiPorts');

const getTimezone = async (endPoint, id) => {
  const { inventoryToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/timezone`;
  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
}

module.exports = {
  getTimezone
};
