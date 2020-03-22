import React from 'react';
import { Modal } from '@grafana/ui';

export const ItemModal = (props: any) => {
  const { showItemModal, setItemModal, convertedData, selectedItem } = props;
  const itemData = convertedData.filter((item: any) => item.id === selectedItem);

  return (
    <Modal
      title={
        <div className="modal-header-title" style={{ padding: '10px 0' }}>
          <i className="fa fa-info-circle" />
          <span className="p-l-1">Item data</span>
        </div>
      }
      isOpen={showItemModal}
      onDismiss={() => setItemModal(false)}
      className="inventroy-modal"
    >
      {itemData[0] && Object.keys(itemData[0]).filter(key => key !== 'id').map(key =>
        <div style={{ width: 'auto' }} key={key}>
          <p style={styles.itemData}>
            <span style={styles.itemFont}>{key}</span>: {itemData[0][key]}
          </p>
        </div>
      )}
    </Modal>
  );
};

const styles = {
  itemData: {
    background: '#212124',
    padding: '15px 10px',
    marginBottom: 5,
  },
  itemFont: {
    fontWeight: 'bold' as 'bold',
  },
};
