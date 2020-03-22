const { callApi } = require('../../services/restApi');
const { POST } = require('../../constants/apiMethods');
const { INVENTORY } = require('../../constants/apiPorts');

const getAuthTokens = async (endPoint, calipsoPassword) => {
  url = `https://${endPoint}:${INVENTORY}/auth/tokens`;

  const body = {
    auth: {
      methods: ["credentials"],
      credentials: {
        username: "calipso",
        password: calipsoPassword,
      }
    },
  };

  return await callApi(url, POST, body);
}

module.exports = {
  getAuthTokens
};
