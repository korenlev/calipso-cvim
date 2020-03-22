const express = require('express');
const router = express.Router();

const { fetchEnvironmentConfigs, fetchObjectTypes, fetchInventory, fetchScans, fetchScheduledScans } = require('../grafana_handlers/inventory');

router.all('/', (req, res, next) => {
  try {
    res.status(200).end();
  } catch (error) {
    res.status(500).json({status: 'error-requesting-grafana-test'});
  }
});

router.all('/search', async (req, res, next) => {
  const target = req.body.target;
  const endPoint = podsEndPoints[0];

  let response, data = [];

  try {
    switch (target) {
      case 'environment_configs':
        response = await fetchEnvironmentConfigs(endPoint);
        response = response.environment_configs;
        response.map(({name}) => {
          data = [...data, name];
        });
        break;
      case 'object_types':
        response = await fetchObjectTypes(endPoint);
        response = response.data;
        response.map(({value}) => {
          data = [...data, value];
        });
        break;
    }

    res.json(data);
  } catch (error) {
    res.status(500).json({status: 'error-requesting-grafana-search'});
  }
});

router.all('/query', async (req, res, next) => {
  // const target = req.body.targets[0].target;
  let data = [], environment, fields, objectType;
  const range = req.body.range;
  const endPoint = podsEndPoints[0];
  const type = req.body.targets[0].type;

  try {
    switch (type) {
      case 'inventory':
        objectType = req.body.scopedVars.object_types.value;
        fields = req.body.targets[0].typeFields && req.body.targets[0].typeFields[objectType] || '';
        environment = req.body.scopedVars.environment_configs.value;

        data = await fetchInventory(endPoint, environment, objectType, fields, range);
        break;
      case 'scans':
        environment = req.body.scopedVars.environment_configs.value;
        data = await fetchScans(endPoint, environment);
        break;
      case 'scheduled_scans':
        environment = req.body.scopedVars.environment_configs.value;
        data = await fetchScheduledScans(endPoint, environment);
        break;
    }

    res.json(data);
  } catch (error) {
    console.log(error);
    res.status(500).json({status: 'error-requesting-grafana-query'});
  }
});


router.all('/annotations', (req, res, next) => {
  try {
    res.json({});
  } catch (error) {
    res.status(500).json({status: 'error-requesting-grafana-annotations'});
  }
});

module.exports = router;
