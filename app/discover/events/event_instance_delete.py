import re

from bson.objectid import ObjectId

from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class EventInstanceDelete(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
        # find the corresponding object
        id = values['instance_id']
        item = self.inv.get_by_id(env, id)
        if not item:
            self.log.info('instance document not found, aborting instance delete')
            return None
        db_id = ObjectId(item['_id'])
        id_path = item['id_path'] + '/'
        # remove related clique
        clique_finder = self.inv.get_clique_finder()
        self.inv.delete('cliques', {'focal_point': db_id})

        # keep related links to do rebuild of cliques using them
        matched_links = clique_finder.find_links_by_source(db_id) + clique_finder.find_links_by_target(db_id)
        links_using_object = [l['_id'] for l in matched_links]

        # find cliques using these links
        matched_cliques = clique_finder.find_cliques_by_link({'links': {'$in': links_using_object}})
        # find cliques using these links and rebuild them
        for clique in matched_cliques:
            clique_finder.rebuild_clique(clique)

        # remove all related links
        self.inv.delete('links', {'source': db_id})
        self.inv.delete('links', {'target': db_id})

        # remove object itself
        self.inv.delete('inventory', {'_id': db_id})

        # remove objects under the object
        regexp = re.compile('^' + id_path)
        self.inv.delete('inventory', {'id_path': {'$regex': regexp}})
