const { callApi } = require('../../services/restApi');
const { GET } = require('../../constants/apiMethods');
const { CISCOVIM } = require('../../constants/apiPorts');

const getSetupData = async (endPoint, token) => {
  url = `https://${endPoint}:${CISCOVIM}/setupdata`;

  const headers = {
    Authorization: token,
  };

  return await callApi(url, GET, null, headers);
}

module.exports = {
  getSetupData
};
