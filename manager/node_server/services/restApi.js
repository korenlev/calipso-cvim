const fetch = require('node-fetch');
const AbortController = require('node-abort-controller');

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

const callApi = async (url, method, body, headers = {}, timeout = 5000) => {
  const controller = new AbortController();
  setTimeout(() => controller.abort(), timeout);

  headers['Content-Type'] = 'application/json';

  const options = {
    method,
    headers,
    signal: controller.signal,
  };

  if (body) {
    options.body = JSON.stringify(body);
  }

  return fetch(url, options).then((response) => response.json());
}

module.exports = {
  callApi
};
