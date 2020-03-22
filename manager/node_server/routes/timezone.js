const express = require('express');
const router = express.Router();

const { getTimezone } = require('../requests/inventory/timezone');

router.get('/', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const timeZone = await getTimezone(endPoint);
    res.status(200).json(timeZone);
  }
  catch (error) {
    res.status(500).json({status: 'error-requesting-timezone'});
  }
});

module.exports = router;
