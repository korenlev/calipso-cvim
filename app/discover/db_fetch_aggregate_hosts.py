from discover.db_access import DbAccess


class DbFetchAggregateHosts(DbAccess):
    def get(self, id):
        query = """
      SELECT CONCAT('aggregate-', a.name, '-', host) AS id, host AS name
      FROM nova.aggregate_hosts ah
        JOIN nova.aggregates a ON a.id = ah.aggregate_id
      WHERE ah.deleted = 0 AND aggregate_id = %s
    """
        return self.get_objects_list_for_id(query, "host", id)
