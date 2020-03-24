import React from 'react';
import { Modal } from '@grafana/ui';

export const ScansModal = (props: any) => {
  const { showScansModal, setScansModal } = props;

  return (
    <Modal
      title={
        <div className="modal-header-title" style={{ padding: '10px 0' }}>
          <i className="fa fa-info-circle" />
          <span className="p-l-1">Discovery Scheduling</span>
        </div>
      }
      isOpen={showScansModal}
      onDismiss={() => setScansModal(false)}
      className="inventroy-modal"
    ></Modal>
  );
};
