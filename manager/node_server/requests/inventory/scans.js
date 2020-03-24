const { callApi } = require('../../services/restApi');
const { GET, POST, DELETE } = require('../../constants/apiMethods');
const { INVENTORY } = require('../../constants/apiPorts');

const getScans = async (endPoint, environment) => {
  const { inventoryToken, podName, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/scans?env_name=${environment}`;

  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
}

const getLatestScan = async endPoint => {
  const { inventoryToken, podName, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/scans?env_name=cvim-${podName}&latest=true`;

  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
}

const getScanLogLevels = async endPoint => {
  const { inventoryToken, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/constants?name=log_levels`;

  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  try {
    return await callApi(url, GET, null, headers);
  } catch(error) {
    console.log('error calling API', error)
  }
  
}

const postScan = async req => {
  const {endPoint, query} = req.body;

  try {
    const { inventoryToken, podUrl } = podsToken[endPoint];
    const url = `https://${podUrl}:${INVENTORY}/scans`;
    const headers = {
      'X-Auth-Token': inventoryToken,
    };

    return await callApi(url, POST, query, headers);
    
  } catch(error) {
    console.log('request error', error)
  }

}

const postScheduledScan = async req => {
  const {endPoint, query} = req.body;
  try {
    const { inventoryToken, podUrl } = podsToken[endPoint];
    const url = `https://${podUrl}:${INVENTORY}/scheduled_scans`;
    const headers = {
      'X-Auth-Token': inventoryToken,
    };

    return await callApi(url, POST, query, headers);
    
  } catch(error) {
    console.log('request error', error)
  }
}

const deleteScheduledScan = async req => {
  const {endPoint, ids} = req.query;
  try {
    const { inventoryToken, podName, podUrl } = podsToken[endPoint];
    const url = `https://${podUrl}:${INVENTORY}/scheduled_scans?env_name=cvim-${podName}&ids=${ids}`;

    const headers = {
      'X-Auth-Token': inventoryToken,
    };

    return await callApi(url, DELETE, {}, headers);
    
  } catch(error) {
    console.log('deleteScheduledScan error', error)
  }
}

const getScheduledScans = async (endPoint, environment) => {
  const { inventoryToken, podName, podUrl } = podsToken[endPoint];
  const url = `https://${podUrl}:${INVENTORY}/scheduled_scans?env_name=${environment}`;
  const headers = {
    'X-Auth-Token': inventoryToken,
  };
  return await callApi(url, GET, null, headers);
}

module.exports = {
  getScans,
  getLatestScan,
  postScan,
  getScheduledScans, 
  getScanLogLevels, 
  postScheduledScan,
  deleteScheduledScan
};
