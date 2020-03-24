const express = require('express');
const router = express.Router();

const { getScans, getLatestScan, postScan, getScanLogLevels } = require('../requests/inventory/scans');

// get scans
router.get('/', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const latestScan = await getScans(endPoint);
    res.status(200).json(latestScan);
  }
  catch (error) {
    res.status(500).json({status: 'scans-not-available'});
  }
});

// get latest scan
router.get('/latest_scans', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const latestScan = await getLatestScan(endPoint);
    res.status(200).json(latestScan);
  }
  catch (error) {
    res.status(500).json({status: 'inventory-scan-not-available'});
  }
});

// get scan log levels
router.get('/log_levels', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const latestScan = await getScanLogLevels(endPoint);
    res.status(200).json(latestScan);
  }
  catch (error) {
    res.status(500).json({status: 'inventory-scan-not-available'});
  }
});

router.post('/', async (req, res, next) => {
  try {
    const scanRequest = await postScan(req)
    res.status(200).json(scanRequest);
  }
  catch (error) {
    res.status(500).json({status: 'scaning-error',error});
  }
});


module.exports = router;
