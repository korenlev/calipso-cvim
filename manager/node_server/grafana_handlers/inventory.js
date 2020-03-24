const { getEnvironmentConfigs, getObjectTypes, getInventoryList } = require('../requests/inventory/inventory');
const { getScans, getScheduledScans } = require('../requests/inventory/scans');

const fetchEnvironmentConfigs = async (endPoint) => {
  return await getEnvironmentConfigs(endPoint);
};

const fetchObjectTypes = async (endPoint) => {
  return await getObjectTypes(endPoint);
};

const fetchInventory = async (endPoint, environment, type, fields, range) => {
  let projection, fieldsArr = [], columns = [];
  const defaultFields = ['id', 'name', 'name_path', 'last_scanned'];

  projection = fields.replace(new RegExp(`(\\s)`, 'g'), '');

  if (projection) {
    fieldsArr = projection.split(',');
  }

  defaultFields.map(field => {
    if (!fieldsArr.includes(field)) {
      fieldsArr = [...fieldsArr, field];
    }
  });
  
  projection = fieldsArr.join();

  const inventoryList = await getInventoryList(endPoint, environment, type, projection);
  let inventoryObjects = inventoryList.objects || [];

  inventoryObjects = inventoryObjects.filter(({last_scanned}) => {
    const testDate = new Date(last_scanned);
    const fromDate = new Date(range.from);
    const toDate = new Date(range.to);

    return fromDate <= testDate && testDate <= toDate
  });

  fieldsArr.map(field => {
    columns = [...columns, {text: field, type: field}];
  });

  const data = [
    {
      target: "inventory",
      columns,
      rows: [],
      type: "table"
    },
  ];

  inventoryObjects.forEach(item => {
    let row = [];
    fieldsArr.map(field => {
      row = [...row, item[field]];
    });
    data[0].rows.push(row);
  });

  return data;
};

const fetchScans = async (endPoint, environment) => {
  let scansRows = [];
  let scheduledScansRows = [];

  try {
    const scansList = await getScans(endPoint, environment);
    const scanFields = ['ID','Status','Environment', 'Start timestamp', 'End timestamp'];

    const scanColumns = scanFields.map((field) => {
      return {text:field,type:'string'} 
    })

    if(scansList.error){
      scansRows = [];
    } else {
      scansList.scans.map((row,i) => {
        scansRows.push([
            row.id,
            row.status,
            row.environment,
            row.start_timestamp,
            row.end_timestamp
          ]
        )
      })
    }
    
    const scheduledScansList = await getScheduledScans(endPoint, environment);
    const scheduledScansFields = ['ID','Environment', 'Recurrence', 'Scheduled timestamp'];
    const scheduledScansColumns = scheduledScansFields.map((field) => {
      return {text:field,type:'string'} 
    })    
    
    if(scheduledScansList.error){
      scheduledScansRows = [];
    } else {
      scheduledScansList.scheduled_scans.map((row,i) => {
        scheduledScansRows.push([
          row.id,
          row.environment,
          row.recurrence,
          row.scheduled_timestamp
          ]
        )
      })
    }

    const data = [
      {
        target: "scans",     
        columns: scanColumns,
        rows: scansRows,
        type: "table"
      },
      {
        target: "scheduled_scans",     
        columns:scheduledScansColumns,
        rows:scheduledScansRows,
        type: "table"
      },
    ];

    return data; 
    } catch(error){
      console.log('error getting scans', error)
      return [];
    }  
};

module.exports = {
  fetchEnvironmentConfigs,
  fetchObjectTypes,
  fetchInventory,
  fetchScans
};
