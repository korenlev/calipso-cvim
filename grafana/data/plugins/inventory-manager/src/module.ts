import { PanelPlugin } from '@grafana/data';
import { InventoryManagerOptions, defaults } from './types';
import { InventoryManager } from './InventoryManager';
import { SimpleEditor } from './SimpleEditor';

export const plugin = new PanelPlugin<InventoryManagerOptions>(InventoryManager).setDefaults(defaults).setEditor(SimpleEditor);
