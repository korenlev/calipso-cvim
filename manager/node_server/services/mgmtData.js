const fs = require('fs');
const { MGMT_FILE } = require('../constants/dataFiles');

let mgmtData;

try {
  mgmtData = fs.readFileSync(MGMT_FILE, 'utf8').toString().split("\n");
} catch (error) {
  console.log(error, `\n\n * Try starting the server as the owner of: ${MGMT_FILE}`);
  process.exit();
}

const getEndPoint = () => {
  for (let i = 0; i < mgmtData.length; i++) {
    const regExp = new RegExp(`\\["https://([0-9]+).([0-9]+).([0-9]+).([0-9]+):8445"\\]`);
    if (regExp.test(mgmtData[i])) {
      return [i, mgmtData[i]];
    }
  }
}

const getToken = (index) => {
  for (let i = index; i < mgmtData.length; i++) {
    const regExp = new RegExp(`Authorization`);
    if (regExp.test(mgmtData[i])) {
      return mgmtData[i];
    }
  }
};

const getEndPointData = () => {
  let [index, endPointStr] = getEndPoint();
  let token = getToken(index);

  // cut endPoint
  endPointStr = endPointStr
    .trim()
    .replace('urls = ["', '')
    .replace('"]', '')
    .replace('http://', '')
    .replace('https://', '');
  const [endPoint, _] = endPointStr.split(':');

  // cut Authorization token
  token = token
    .trim()
    .replace('Authorization = "', '')
    .replace('"', '');

  return {
    endPoint,
    token,
  };
};

module.exports = {
  getEndPointData,
}
