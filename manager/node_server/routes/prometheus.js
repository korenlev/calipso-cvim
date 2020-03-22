const express = require('express');
const router = express.Router();

const {
  getDiskioReadBytes,
  getAlerts
} = require('../requests/prometheus/diskioReadBytes');

router.get('/diskioReadBytes', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const diskioReadBytes = await getDiskioReadBytes(endPoint);
    res.status(200).json(diskioReadBytes);
  }
  catch (error) {
    res.status(500).json({status: 'error-requesting-diskio-read-bytes'});
  }
});

router.get('/alerts', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const alerts = await getAlerts(endPoint);
    res.status(200).json(alerts);
  }
  catch (error) {
    res.status(500).json({status: 'error-requesting-alerts'});
  }
});

module.exports = router;
