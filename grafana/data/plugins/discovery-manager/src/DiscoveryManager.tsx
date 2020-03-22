import React from 'react';
import { CustomScrollbar, Table, useTheme } from '@grafana/ui';
import { ConfigOverrideRule, PanelProps, DataFrame, GrafanaTheme, MutableDataFrame, applyFieldOverrides } from '@grafana/data';
import DiscoveryForm from './form/DiscoveryForm';

function buildData(fields: any, theme: GrafanaTheme, overrides: ConfigOverrideRule[]): DataFrame {
  const data = new MutableDataFrame({
    fields:fields
  });

  return applyFieldOverrides({
    data: [data],
    fieldOptions: {
      overrides,
      defaults: {},
    },
    theme,
    replaceVariables: (value: string) => value,
  })[0];
}

interface Props extends PanelProps {}

export const DiscoveryManager = (props:Props) => {
  const theme = useTheme();
  const { data: { series }} = props;
  const scansData = series.length?buildData(series[0].fields, theme, []):[];
  const scheduledScansData = series.length?buildData(series[1].fields, theme, []):[];

  return (
    <CustomScrollbar>
      <div style={styles.container}>
        <DiscoveryForm environment={props.data.request?.scopedVars.environment_configs.value} />
        {scansData.length > 0 &&
        <div style={styles.tableSection}>
          <h2>Scans</h2>
          <div id="cisco-panel-container" className="panel-container" style={{ width: 'auto' }}>
            <Table data={scansData} height={400} width={865} />
          </div>
        </div>
        }
        {scheduledScansData.length > 0 &&
        <div style={styles.tableSection}>
          <h2>Scheduled Scans</h2>
          <div id="cisco-panel-container" className="panel-container" style={{ width: 'auto' }}>
            <Table data={scheduledScansData} height={400} width={865} />
          </div>
        </div>
        }
      </div>      
    </CustomScrollbar>
  );
};

const styles = {
  container: {
    padding: 60, 
    display: 'flex', 
    flexDirection: 'column',
    justifyContent: 'center', 
    alignItems: 'center'
  },
  tableSection: {
    padding: '30px 0',
  },
}
