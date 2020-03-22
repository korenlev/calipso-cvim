const express = require('express');
const router = express.Router();

const { postScheduledScan, getScheduledScan, deleteScheduledScan } = require('../requests/inventory/scans');

router.get('/', async (req, res, next) => {
  try {
    const endPoint = req.query.endPoint;
    const scanRequest = await getScheduledScan(endPoint)
    
    res.status(200).json(scanRequest);
  }
  catch (error) {
    res.status(500).json({status: 'scaning-error',error});
  }
});

router.post('/', async (req, res, next) => {
  try {
    const scanRequest = await postScheduledScan(req)
    res.status(200).json(scanRequest);
  }
  catch (error) {
    res.status(500).json({status: 'scaning-error',error});
  }
});

router.delete('/', async (req, res, next) => {
  try {
    const deleteScan = await deleteScheduledScan(req)
    res.status(200).json(deleteScan);
  }
  catch (error) {
    res.status(500).json({status: 'scaning-error',error});
  }
});


module.exports = router;
