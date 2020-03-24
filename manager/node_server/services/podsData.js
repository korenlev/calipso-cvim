const { getEndPointData } = require('./mgmtData');
const { getSetupData } = require('../requests/ciscovim/setupData');
const {
  getCalipsoApiServicePwd,
  getCvimMonServerPassword } = require('../requests/ciscovim/calipsoSecrets');
const { getAuthTokens } = require('../requests/inventory/authTokens');

podsToken = {}, podsEndPoints = [];

const initPodsData = async () => {
  // Start time
  const startTime = [Date.now()];

  let currentSetupData, externalAddress, podName, calipsoApiServicePwd, cvimMonServerPassword;

  let { endPoint, token } = getEndPointData();
  
  // Get setup data
  console.log(`${[Date.now()]} - Get setup data...`);
  try {
    const setupDatas = await getSetupData(endPoint, token);
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
    const calipsoApiServicePwdResults = await getCalipsoApiServicePwd(endPoint, token);
    calipsoApiServicePwd = calipsoApiServicePwdResults.CALIPSO_API_SERVICE_PWD;
    console.log(`${[Date.now()]} - OK`);
  } catch (error) {
    console.log(`${[Date.now()]} - ${error}`);
  }

  // Get auth tokens
  let authResults, inventoryToken, podUrl;
  try {
    console.log(`${[Date.now()]} - Get auth tokens by using endPoint...`);
    authResults = await getAuthTokens(endPoint, calipsoApiServicePwd);
    inventoryToken = authResults.token;
    podUrl = endPoint;
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
    const cvimMonServerPasswordResults = await getCvimMonServerPassword(endPoint, token);
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
  
  if(!endPoint) {
    return;
  }

  podsToken = {
    [endPoint]: {
      inventoryToken,
      prometheusToken,
      podName,
      podUrl,
    },
  };

  podsEndPoints = [...podsEndPoints, endPoint];

  // Conclusions
  console.log(`${[Date.now()]} - OK - ${JSON.stringify(podsToken)}`);
  console.log(`${[Date.now()]} - OK - ${JSON.stringify(podsEndPoints)}`)
  console.log(`\nTime: ${[Date.now()] - startTime}ms.\n`);
};

module.exports = {
  initPodsData,
};
