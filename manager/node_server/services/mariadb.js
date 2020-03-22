const mariadb = require('mariadb');
const { getVal } = require('./envData');

const initDatabase = () => {
  pool = mariadb.createPool({
    host: getVal('DB_SERVER_IP'),
    user:'root', 
    password: getVal('DB_SERVER_PASSWORD'),
    database: 'rbac',
    connectionLimit: 5
  });
}

module.exports = {
  initDatabase,
};
