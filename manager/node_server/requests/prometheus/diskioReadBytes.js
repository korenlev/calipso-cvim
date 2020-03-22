const { callApi } = require('../../services/restApi');
const { GET } = require('../../constants/apiMethods');
const { PROMETHEUS } = require('../../constants/apiPorts');

const getDiskioReadBytes = async (endPoint, host) => {
  const { prometheusToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${PROMETHEUS}/api/v1/query?query=diskio_read_bytes{host="ntn01-vim-stor-04"}`;
  const headers = {
    Authorization: prometheusToken,
  };
  return await callApi(url, GET, null, headers);
}

const getAlerts = async (endPoint, host) => {
  const { prometheusToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${PROMETHEUS}/api/v1/alerts?query={severity="warning"}`;
  const headers = {
    Authorization: prometheusToken,
  };
  return await callApi(url, GET, null, headers);
}

module.exports = {
  getDiskioReadBytes,
  getAlerts,
};
