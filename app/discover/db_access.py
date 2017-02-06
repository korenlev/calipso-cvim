import mysql.connector

from discover.configuration import Configuration
from discover.fetcher import Fetcher
from discover.util import Util


class DbAccess(Fetcher, Util):
    conn = None
    query_count_per_con = 0

    def __init__(self):
        super().__init__()
        self.config = Configuration()
        self.conf = self.config.get("mysql")
        self.connect_to_db()
        cursor = DbAccess.conn.cursor(dictionary=True)
        try:
            # check if DB schema 'neutron' exists
            cursor.execute("SELECT COUNT(*) FROM neutron.agents")
            for row in cursor:
                pass
            self.neutron_db = "neutron"
        except (AttributeError, mysql.connector.errors.ProgrammingError):
            self.neutron_db = "ml2_neutron"

    def db_connect(self, _host, _port, _user, _password, _database):
        if DbAccess.conn:
            return
        try:
            # connection timeout set to 30 seconds,
            # due to problems over long connections
            TIMEOUT = 30
            DbAccess.conn = mysql.connector.connect(host=_host, port=_port,
                                                    connection_timeout=TIMEOUT,
                                                    user=_user,
                                                    password=_password,
                                                    database=_database,
                                                    raise_on_warnings=True)
            DbAccess.conn.ping(True)  # auto-reconnect if necessary
        except:
            self.log.critical("failed to connect to MySQL DB")
            return
        DbAccess.query_count_per_con = 0

    def connect_to_db(self, force=False):
        if DbAccess.conn:
            if not force:
                return
            self.log.info("DbAccess: ****** forcing reconnect, " +
                          "query count: %s ******",
                          DbAccess.query_count_per_con)
            DbAccess.conn = None
        self.conf = self.config.get("mysql")
        cnf = self.conf
        self.db_connect(cnf["host"], cnf["port"],
                        cnf["user"], cnf["password"],
                        cnf["schema"])

    def get_objects_list_for_id(self, query, object_type, id):
        self.connect_to_db(DbAccess.query_count_per_con >= 25)
        DbAccess.query_count_per_con += 1
        self.log.debug("query count: %s, running query:\n%s\n",
                       str(DbAccess.query_count_per_con), query)

        cursor = DbAccess.conn.cursor(dictionary=True)
        try:
            if id:
                cursor.execute(query, [str(id)])
            else:
                cursor.execute(query)
        except (AttributeError, mysql.connector.errors.OperationalError) as e:
            self.log.error(e)
            self.connect_to_db(True)
            # try again to run the query
            cursor = DbAccess.conn.cursor(dictionary=True)
            if id:
                cursor.execute(query, [str(id)])
            else:
                cursor.execute(query)

        rows = []
        for row in cursor:
            rows.append(row)
        return rows

        if isinstance(object_type, str):
            ret = {"type": object_type, "rows": rows}
        else:
            # object_type is a hash of parameters, just add "rows" to it
            ret = object_type
            ret["rows"] = rows

        return ret

    def get_objects_list(self, query, object_type):
        return self.get_objects_list_for_id(query, object_type, None)

    def get_objects(self, qry, type, id):
        return self.jsonify(self.get_objects_list(qry, type))

    def get(self, id):
        # return list of available fetch types
        ret = {
            "description": "List of available fetch calls for this interface",
            "types": {
                "regions": "Regions of this environment",
                "projects": "Projects (tenants) of this environment",
                "availability_zones": "Availability zones",
                "aggregates": "Host aggregates",
                "aggregate_hosts": "Hosts in aggregate X (parameter: id)",
                "az_hosts": "Host in availability_zone X (parameter: id)"
            }
        }
        return self.jsonify(ret)

    def exec(self, query, table, field, values):
        try:
            cursor = DbAccess.conn.cursor(dictionary=True)
            cursor.execute(query, [table, field, values])
        except (AttributeError, mysql.connector.errors.OperationalError) as e:
            self.log.error(e)
            self.connect_to_db(True)
            # try again to run the query
            cursor = DbAccess.conn.cursor(dictionary=True)
            cursor.execute(query, [table, field, values])

        rows = []
        for row in cursor:
            rows.append(row)
        return rows

    def set(self, table, field, values):
        query = """INSERT INTO %s %s VALUES %s"""
        return self.exec(query, table, field, values)

    def delete(self, table, field, values):
        query = """DELETE FROM %s WHERE %s=%s"""
        return self.exec(query, table, field, values)
