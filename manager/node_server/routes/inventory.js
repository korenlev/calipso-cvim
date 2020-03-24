const express = require('express');
const router = express.Router();

const { getInventoryList, getInventoryItem, getEnvironmentConfigs } = require('../requests/inventory/inventory');

router.get('/inventory', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  const inventoryList = await getInventoryList(endPoint);
  const inventoryObjects = inventoryList.objects;

  let response = [];

  for (let item of inventoryObjects) {
    const { id } = item;
    const inventoryItem = await getInventoryItem(endPoint, id);
    response = [...response, inventoryItem];
  }

  res.status(200).json(response);
});

router.get('/environment_configs', async (req, res, next) => {
  const endPoint = req.query.endPoint;
  try {
    const environment_configs = await getEnvironmentConfigs(endPoint);
    res.status(200).json(environment_configs);
  }
  catch (error) {
    res.status(500).json({status: 'environment_configs-not-available'});
  }
});

module.exports = router;
