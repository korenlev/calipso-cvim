export class GenericDatasourceQueryCtrl {
  static templateUrl = 'partials/query.editor.html';

  target: any;
  panelCtrl: any;
  datasource: any;
  types: object[];
  objectTypes: object[];

  constructor() {
    this.types = [
      { text: '', value: '' },
      { text: 'Inventory', value: 'inventory' },
      { text: 'Scans', value: 'scans' },
    ];

    this.objectTypes = [];

    this.findMetrics('object_types').then((results:any) =>{
      this.objectTypes = results;
    });
  }

  onChangeInternal() {
    this.panelCtrl.refresh();
  }

  findMetrics(query: string) {
    return this.datasource.metricFindQuery(query);
  }

  showInventory() {
    return this.target.type === 'inventory';
  }

  showFieldType(fieldType: string) {
    return fieldType === this.target.objectType;
  }
}
