import React, { useState } from 'react';
import { Button, Input, Switch, Select } from '@grafana/ui';
import {FieldValidationMessage} from '../../../../../packages/grafana-ui/src/components/Forms/FieldValidationMessage'
import DatePicker from 'react-datepicker';
import {ApiConnect} from '../Helpers';
import RouteTypes from '../constants/RouteTypes';  
import ValidationTypes from '../constants/ValidationTypes';  
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import "react-datepicker/dist/react-datepicker.css";
import "../styles/styles.scss"

const recurrenceData = [
  { value: 'HOURLY', label: 'HOURLY' },
  { value: 'ONCE', label: 'ONCE' },
  { value: 'DAILY', label: 'DAILY' },
  { value: 'WEEKLY', label: 'WEEKLY' },
  { value: 'MONTHLY', label: 'MONTHLY' },
  { value: 'YEARLY', label: 'YEARLY' },
];

const logLevelsData = [
  { value: 'critical', label: 'CRITICAL' },
  { value: 'error', label: 'ERROR' },
  { value: 'warning', label: 'WARNING' },
  { value: 'info', label: 'INFO' },
  { value: 'debug', label: 'DEBUG' },
  { value: 'notset', label: 'NOTSET' },
];

interface errors {
  reccurence: string; 
  logLevel: string; 
}

interface Props {
  environment: string
}

const DiscoveryForm = ({environment}:Props) => {
  const [reccurence, setReccurence] = useState<string>();
  const [scanTimestamp, setScanTimestamp] = useState<Date>(new Date());
  const [scanNow, setScanNow] = useState<boolean>(false);
  const [logLevel, setLogLevel] = useState<string>();
  const [clearData, setClearData] = useState<boolean>(true);
  const [scanOnlyInventory, setScanOnlyInventory] = useState<boolean>(false);
  const [scanOnlyLinks, setScanOnlyLinks] = useState<boolean>(false);
  const [scanOnlyCliques, setScanOnlyCliques] = useState<boolean>(false);
  const [elasticSearch, setElasticSearch] = useState<boolean>(false);
  const [errors, setErrors] = useState<any>();
  const [formSubmited, setFromSubmited] = useState<boolean>();

  const setGroupCheckbox = (value:string) => {
    setScanOnlyInventory(false);
    setScanOnlyLinks(false);
    setScanOnlyCliques(false);
    switch (value) {
      case 'scanOnlyInventory':
        setScanOnlyInventory(true);
        break;
      case 'scanOnlyLinks':
        setScanOnlyLinks(true);
      break;
      case 'scanOnlyCliques':
        setScanOnlyCliques(true);
      break;
    }
  }

  const scanNowOnChange = (e:any) => {
    setScanNow(e.currentTarget.checked);
    setReccurence('once');
    setScanTimestamp(new Date()); 
  }

  const onReccurenceChange = (value:any) => {
    setErrors({
      ...errors, 
      reccurence: ''
  })
    setReccurence(value);
  }

  const onLoglevelChange = (value:any) => {
    setErrors({
      ...errors, 
      logLevel: ''
  })
    setLogLevel(value);
  }
  
  const validateForm = (e:any) => {
    e.preventDefault();
    const errors = {} as errors; 
  
    if(reccurence === undefined){
      errors.reccurence = ValidationTypes.REQUIRED
    }
    if(logLevel === undefined){
      errors.logLevel = ValidationTypes.REQUIRED
    }
    if(Object.keys(errors).length > 0){
      setErrors(errors)
    } else {
      setFromSubmited(true)
      createNewScan()
    }
  }

  const createNewScan = () => {
    const req:any = {
      query: {
        log_level: logLevel,
        clear: clearData,
        scan_only_links: scanOnlyLinks,
        scan_only_cliques: scanOnlyCliques,
        scan_only_inventory: scanOnlyInventory,
        env_name: environment,
        es_index: elasticSearch
      },
      endPoint:'172.28.123.140'
    }

    if(!scanNow){
      req.query.recurrence = reccurence; 
      req.query.scheduled_timestamp = new Date(scanTimestamp).toISOString().slice(0,-1);
    }

    const route = !scanNow ? RouteTypes.SCHEDULED_SCANS : RouteTypes.SCANS;  

    ApiConnect(route,req)
    .then((res) => {
      setFromSubmited(false)
      if(res.error){
        toast.error(res.error.message, {
          position: toast.POSITION.TOP_CENTER
        })
      } else {
        toast.success(res.message, {
          position: toast.POSITION.TOP_CENTER
        })
      }      
    }).catch((error) => {
      setFromSubmited(false)
      toast.error("Something went wrong", {
        position: toast.POSITION.TOP_CENTER
      })
    })
  }

  return (
    <div>
      <div>
        <div>
          <h2>Discovery Scheduling</h2>
        </div>
        <form>
          <section style={styles.section}>
            <div style={styles.select}>
            <Input value={environment} disabled />
            </div>
            <div style={styles.select}>
              <Select 
                placeholder="Reccurence" 
                options={recurrenceData} 
                onChange={({ value }) => onReccurenceChange(value)} 
                value={recurrenceData.filter((val) => val.value === reccurence)}
                isDisabled={scanNow}
              />
              { errors && errors.reccurence  &&
                <FieldValidationMessage 
                children={errors.reccurence}
              />
              }
            </div>
            <div>
               <DatePicker
                placeholder="Schedule Scan"
                selected={scanTimestamp}
                onChange={(val:any) => setScanTimestamp(val)}
                showTimeSelect
                dateFormat="Pp"
                disabled={scanNow}
              />
            </div>
            <div style={styles.scanNow}>
              <Switch onChange={scanNowOnChange} label="Now" checked={scanNow} />
            </div>
            <div style={styles.select}>
              <Select 
                placeholder="Log Level" 
                options={logLevelsData} 
                onChange={({ value }) => onLoglevelChange(value)} 
                />
                { errors && errors.logLevel  &&
                <FieldValidationMessage 
                children={errors.logLevel}
              />
              }
            </div>
          </section>
          <section>
            <div style={styles.section}>
              <Switch onChange={e => setClearData(e ? e.currentTarget.checked : false)} label="Clear Data" checked={clearData} />
              <Switch onChange={e => scanOnlyInventory? setScanOnlyInventory(false): setGroupCheckbox('scanOnlyInventory')} label="Scan Only Inventory" checked={scanOnlyInventory} />
              <Switch onChange={e => scanOnlyLinks? setScanOnlyLinks(false): setGroupCheckbox('scanOnlyLinks')} label="Scan Only Links" checked={scanOnlyLinks} />
              <Switch onChange={e => scanOnlyCliques? setScanOnlyCliques(false): setGroupCheckbox('scanOnlyCliques')} label="Scan Only Cliques" checked={scanOnlyCliques} />
              <Switch onChange={e => setElasticSearch(e ? e.currentTarget.checked : false)} label="Elastic Search Indexing" checked={elasticSearch} />
            </div>
          </section>
          <section>
            <div style={styles.section}>
              <Button 
                type="submit"
                onClick={validateForm}
                disabled={formSubmited}
                >Scan Now</Button>
            </div>
          </section>
        </form>
      </div>
      <ToastContainer />
    </div>
  );
};

const styles = {
  section: {
    display: 'flex',
    justifyContent: 'flex-start',
    padding: '10px 0',
  },
  select: {
    width: 200,
    paddingRight: 20,
  },
  tableSection: {
    padding: '30px 0',
  },
  scanNow: {
    paddingRight: 20
  }
};

export default DiscoveryForm; 