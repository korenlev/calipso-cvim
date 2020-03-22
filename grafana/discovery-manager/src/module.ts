import { PanelPlugin } from '@grafana/data';
import { DiscoveryManagerOptions, defaults } from './types';
import { DiscoveryManager } from './DiscoveryManager';
import { SimpleEditor } from './SimpleEditor';

export const plugin = new PanelPlugin<DiscoveryManagerOptions>(DiscoveryManager).setDefaults(defaults).setEditor(SimpleEditor);
