import json

from discover.cli_fetch_vconnectors_ovs import CliFetchVconnectorsOvs
from discover.db_access import DbAccess


class CliFetchVconnectorsLxb(CliFetchVconnectorsOvs, DbAccess):

    def __init__(self):
        super().__init__()

    def get(self, id):
        ret = super().get(id)
        for doc in ret:
            query = """
              SELECT configurations
              FROM {}.agents
              WHERE agent_type="Linux bridge agent" AND host = %s
            """.format(self.neutron_db)
            host = doc['host']
            matches = self.get_objects_list_for_id(query, '', host)
            if matches is None:
                raise ValueError('No Linux bridge agent in DB for host' + host)
            agent = matches[0]
            doc['configurations'] = json.loads(agent['configurations'])
        return ret
