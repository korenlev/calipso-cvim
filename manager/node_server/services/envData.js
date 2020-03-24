const { ENV_FILE } = require('../constants/dataFiles');

const fs = require('fs');
const insightEnvData = fs.readFileSync(ENV_FILE, 'utf8').toString().split("\n");

const removeQuotes = (val) => {
  let str = val;
  if (str[0] === '"') {
    str = str.substr(1);
  }
  if (str[str.length-1] === '"') {
    str = str.substr(0, str.length-1);
  }
  return str;
}

const getVal = (req) => {
  for (i in insightEnvData) {
    const [key, value] = insightEnvData[i].split("=");

    if (key === req) {
      return removeQuotes(value);
    }
  }
}

module.exports = {
  getVal,
}
