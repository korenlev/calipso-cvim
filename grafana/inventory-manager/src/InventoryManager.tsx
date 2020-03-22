import React, { useState } from 'react';
import { Input, CustomScrollbar } from '@grafana/ui';
import { ItemModal } from './modal/ItemModal';
import './styles/styles.scss';

export const InventoryManager = (props: any) => {
  const [filter, setFilter] = useState<string>('');
  const [showItemModal, setItemModal] = useState<boolean>(false);
  const [selectedItem, setSelectedItem] = useState<string>('');
  
  const objectType = props.data.request.scopedVars.object_types.value;

  const handleChange = (event: any) => {
    setFilter(event.target.value);
  };

  const convertData = (series: any) => {
    let data: any[] = [];
    if (!series[0]) {
      return data;
    }

    for (let i = 0; i < series[0].length; i++) {
      const obj: any = {};
      series[0].fields.forEach((field: any) => {
        obj[field.name] = field.values.buffer[i];
      });
      data = [...data, obj];
    }
    return data;
  };

  const {
    data: { series },
  } = props;

  const convertedData = convertData(series);

  const openItemModal = (id: string) => {
    setItemModal(true);
    setSelectedItem(id);
  };

  return (
    <CustomScrollbar>
      <div style={styles.container}>
        <div style={styles.fieldWrap}>
          <Input value={filter} onChange={e => handleChange(e)} placeholder="Search..." />
        </div>
      </div>
      <div style={styles.itemContainer}>
        {convertedData
          .filter(val => filter === '' || val.name.toLowerCase().includes(filter.toLowerCase()))
          .map(({ id, name, last_scanned }) => (
            <div
              key={id}
              style={{
                margin: 10,
                padding: 10,
                flex: '0 0 18%',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                alignItems: 'center',
                border: '1px solid rgb(66, 67, 69)',
                borderRadius: 4,
                cursor: 'pointer',
              }}
              onClick={() => {
                openItemModal(id);
              }}
            >
              <h1 style={{ textAlign: 'center', fontSize: '20px', padding: '10px 0' }}>{name}</h1>
              <img src={getImageByType(objectType)} style={{ textAlign: 'center', width: '100px', marginBottom: '20px' }} />
              <p style={{ textAlign: 'center', padding: 10 }}>Last Scanned<br />{new Date(last_scanned).toLocaleString()}</p>
            </div>
          ))}
      </div>
      <ItemModal showItemModal={showItemModal} setItemModal={setItemModal} convertedData={convertedData} selectedItem={selectedItem} />
    </CustomScrollbar>
  );
};

const getImageByType = (objectType: string) => {
  let image;
  try {
    image = require(`./img/icons/${objectType}.png`)
  } catch (error) {};
  try {
    image = require(`./img/icons/${objectType}.jpg`);
  } catch (error) {};
  try {
    image = require(`./img/icons/${objectType}.svg`);
  } catch (error) {};
  return image;
}

const styles = {
  container: {
    padding: 60,
    display: 'flex',
    justifyContent: 'center',
  },
  select: {
    margin: '0 10px',
    height: 50,
    padding: '0 12px',
  },
  itemContainer: {
    display: 'flex',
    justifyContent: 'center',
    flexWrap: 'wrap' as 'wrap',
  },
  filterInput: {
    margin: '0 10px',
    height: 50,
    padding: '0 12px',
  },
  fieldWrap: {
    width: 200,
    margin: '0 20px',
  },
};
