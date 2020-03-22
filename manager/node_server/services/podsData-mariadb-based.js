const { fetchBuildnodeMaster } = require('../db_queries/fetchPods');
const { getSetupData } = require('../requests/ciscovim/setupData');
const {
  getCalipsoApiServicePwd,
  getCvimMonServerPassword } = require('../requests/ciscovim/calipsoSecrets');
const { getAuthTokens } = require('../requests/inventory/authTokens');

podsToken = {};

const initPodsData = async () => {
  // Start time
  const startTime = [Date.now()];

  // Fetch pods data from DB
  const rows = await fetchBuildnodeMaster();

  // Iterate pods and fetch data
  for (i in rows) {
    const { buildnode_name, location } = rows[i];
    console.log(`${[Date.now()]} - Name: ${buildnode_name} - Location: ${location}`);

    const res = await getPodData(rows[i]);

    if (res) {
      podsToken = {...podsToken, ...res};
    }
  }

  // Conclusions
  console.log(`${[Date.now()]} - OK - ${JSON.stringify(podsToken)}`);
  console.log(`\nTime: ${[Date.now()] - startTime}ms.`);
}

const getPodData = async (row) => {
  let currentSetupData, externalAddress, podName, calipsoApiServicePwd, cvimMonServerPassword;

  const { rest_username, rest_password, end_point } = row;

  // Generate auth token
  console.log(`${[Date.now()]} - Generate auth token...`);
  const encodedString = new Buffer.from(`${rest_username}:${rest_password}`).toString('base64');
  const token = `Basic ${encodedString}`;
  console.log(`${[Date.now()]} - OK - ${token}`);
    
  // Get setup data
  console.log(`${[Date.now()]} - Get setup data...`);
  try {
    const setupDatas = await getSetupData(end_point, token);
    setupDatas.setupdatas.forEach(async setupData => {
      if (setupData.status === 'Active') {
        currentSetupData = setupData;
      }
    });
    console.log(`${[Date.now()]} - OK - uuid: ${currentSetupData.uuid}`);
  } catch (error) {
    console.log(`${[Date.now()]} - ${error}`);
  }

  // Parse jsondata and extract details
  console.log(`${[Date.now()]} - Parse jsondata and extract details...`);
  try {
    const parsedJSON = JSON.parse(currentSetupData.jsondata);
    externalAddress = parsedJSON.external_lb_vip_address;
    podName = parsedJSON.PODNAME;
    console.log(`${[Date.now()]} - OK - externalAddress: ${externalAddress} - podName: ${podName}`);
  } catch (error) {
    console.log(`${[Date.now()]} - ${error}`);
  }

  // Get Calipso API service password
  console.log(`${[Date.now()]} - Get Calipso API service password...`);
  try {
    const calipsoApiServicePwdResults = await getCalipsoApiServicePwd(end_point, token);
    calipsoApiServicePwd = calipsoApiServicePwdResults.CALIPSO_API_SERVICE_PWD;
    console.log(`${[Date.now()]} - OK`);
  } catch (error) {
    console.log(`${[Date.now()]} - ${error}`);
  }

  // Get auth tokens
  let authResults, inventoryToken, podUrl;
  try {
    console.log(`${[Date.now()]} - Get auth tokens by using end_point...`);
    authResults = await getAuthTokens(end_point, calipsoApiServicePwd);
    inventoryToken = authResults.token;
    podUrl = end_point;
    console.log(`${[Date.now()]} - OK - ${inventoryToken}`);
  } catch (error) {
    console.log(`${[Date.now()]} - ${error}`);
    try {
      console.log(`${[Date.now()]} - Get auth tokens by using externalAddress...`);
      authResults = await getAuthTokens(externalAddress, calipsoApiServicePwd);
      inventoryToken = authResults.token;
      podUrl = externalAddress;
      console.log(`${[Date.now()]} - OK - ${inventoryToken}`);
    } catch (error) {
      console.log(`${[Date.now()]} - ${error}`);
    }
  }

  // Get CVIMMON server password
  console.log(`${[Date.now()]} - Get CVIMMON server password...`);
  try {
    const cvimMonServerPasswordResults = await getCvimMonServerPassword(end_point, token);
    cvimMonServerPassword = cvimMonServerPasswordResults.CVIM_MON_SERVER_PASSWORD;
    console.log(`${[Date.now()]} - OK`);
  } catch (error) {
    console.log(`${[Date.now()]} - ${error}`);
  }

  // Generate Prometheus auth token
  console.log(`${[Date.now()]} - Generate Prometheus auth token...`);
  const encodedStringPrometheus = new Buffer.from(`admin:${cvimMonServerPassword}`).toString('base64');
  const prometheusToken = `Basic ${encodedStringPrometheus}`;
  console.log(`${[Date.now()]} - OK - ${prometheusToken}`);
  
  if(!end_point) {
    return;
  }

  return {
    [end_point]: {
      inventoryToken,
      prometheusToken,
      podName,
      podUrl,
    },
  };
};

module.exports = {
  initPodsData,
};
