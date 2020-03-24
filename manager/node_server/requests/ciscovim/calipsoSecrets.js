const { callApi } = require('../../services/restApi');
const { GET } = require('../../constants/apiMethods');
const { CISCOVIM } = require('../../constants/apiPorts');

const getCalipsoApiServicePwd = async (endPoint, token) => {
  url = `https://${endPoint}:${CISCOVIM}/secrets/CALIPSO_API_SERVICE_PWD`;

  const headers = {
    Authorization: token,
  };

  return await callApi(url, GET, null, headers);
}

const getCvimMonServerPassword = async (endPoint, token) => {
  url = `https://${endPoint}:${CISCOVIM}/secrets/CVIM_MON_SERVER_PASSWORD`;

  const headers = {
    Authorization: token,
  };

  return await callApi(url, GET, null, headers);
}

module.exports = {
  getCalipsoApiServicePwd,
  getCvimMonServerPassword,
};
