from utils.inventory_mgr import InventoryMgr


def update_resource_version(inv: InventoryMgr,
                            env: str,
                            method: str,
                            resource_version):
    env_config = inv.find_one(collection='environments_config',
                              search={'name': env})

    listener_kwargs = env_config.get('listener_kwargs', {})
    resource_versions = listener_kwargs.get('resource_versions', {})
    resource_versions[method] = int(resource_version)
    listener_kwargs['resource_versions'] = resource_versions
    env_config['listener_kwargs'] = listener_kwargs

    inv.set(item=env_config,
            collection='environments_config')