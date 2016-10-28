from discover.db_access import DbAccess
from test.fetch.test_fetch import TestFetch
from test.fetch.db_fetch.test_data.db_access import *
from unittest.mock import MagicMock, patch
from test.fetch.db_fetch.mock_cursor import MockCursor


class TestDbAccess(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbAccess()

    @patch("mysql.connector.connect")
    def test_db_connect(self, db_connect):
        # store original connection
        original_connection = DbAccess.conn
        # set the connection none
        DbAccess.conn = None
        # mock the methods
        db_conn = MagicMock()
        db_conn.ping = MagicMock()
        db_connect.return_value = db_conn

        self.fetcher.db_connect(DB_CONFIGS['host'], DB_CONFIGS['port'], DB_CONFIGS['user'],
                                DB_CONFIGS['password'], DB_CONFIGS['schema'])
        # reset connection
        DbAccess.conn = original_connection
        # check whether mysql.connector.connect and mysql.connector.db_ping
        # have been invoked
        self.assertEqual(True, db_connect.called, "connect method haven't been called")
        db_conn.ping.assert_called_once_with(True)

    def test_connect_to_db(self):
        # store original db_connect method
        original_db_connect = self.fetcher.db_connect
        # store original connection
        original_connection = DbAccess.conn
        # set connection None
        DbAccess.conn = None
        self.fetcher.db_connect = MagicMock()
        self.fetcher.connect_to_db()

        self.assertEqual(True, self.fetcher.db_connect.called)
        # reset method and connection
        self.fetcher.db_connect = original_db_connect
        DbAccess.conn = original_connection

    def test_connect_to_db_with_force(self):
        # store original db_connect method
        original_db_connect = self.fetcher.db_connect
        # store original connection
        original_connection = DbAccess.conn
        # set connection None
        DbAccess.conn = "connection"
        self.fetcher.db_connect = MagicMock()
        self.fetcher.connect_to_db(force=True)

        self.assertEqual(True, self.fetcher.db_connect.called)
        # reset method and connection
        self.fetcher.db_connect = original_db_connect
        DbAccess.conn = original_connection

    def test_get_objects_list_for_id_with_id(self):
        mock_cursor = MockCursor(OBJECTS_LIST)
        # store original methods
        original_connnect_to_db = self.fetcher.connect_to_db
        original_cursor = DbAccess.conn.cursor

        # mock methods
        self.fetcher.connect_to_db = MagicMock()
        DbAccess.conn.cursor = MagicMock(return_value=mock_cursor)
        mock_cursor.execute = MagicMock()

        result = self.fetcher.get_objects_list_for_id(QUERY_WITH_ID, OBJECT_TYPE, ID)

        mock_cursor.execute.assert_called_once_with(QUERY_WITH_ID, [ID])
        self.assertNotEqual(result, [], "Can't get objects list")

        # reset methods
        self.fetcher.connect_to_db = original_connnect_to_db
        DbAccess.conn.cursor = original_cursor

    def test_get_objects_list_for_id_without_id(self):
        mock_cursor = MockCursor(OBJECTS_LIST)
        # store original methods
        original_connnect_to_db = self.fetcher.connect_to_db
        original_cursor = DbAccess.conn.cursor

        # mock methods
        self.fetcher.connect_to_db = MagicMock()
        DbAccess.conn.cursor = MagicMock(return_value=mock_cursor)
        mock_cursor.execute = MagicMock()

        result = self.fetcher.get_objects_list_for_id(QUERY_WITHOUT_ID, OBJECT_TYPE, None)

        mock_cursor.execute.assert_called_once_with(QUERY_WITHOUT_ID)
        self.assertNotEqual(result, [], "Can't get objects list")

        # reset methods
        self.fetcher.connect_to_db = original_connnect_to_db
        DbAccess.conn.cursor = original_cursor

    def test_get_objects_list_for_id_with_id_with_exception(self):
        mock_cursor = MockCursor(OBJECTS_LIST)
        # store original methods
        original_connnect_to_db = self.fetcher.connect_to_db
        original_cursor = DbAccess.conn.cursor

        # mock methods
        self.fetcher.connect_to_db = MagicMock()
        # mock exception
        DbAccess.conn.cursor = MagicMock(return_value=mock_cursor)
        mock_cursor.execute = MagicMock(side_effect=[AttributeError, ""])

        result = self.fetcher.get_objects_list_for_id(QUERY_WITH_ID, OBJECT_TYPE, ID)

        self.assertEqual(mock_cursor.execute.call_count, 2, "Can't invoke execute method twice when error occurs")
        self.assertNotEqual(result, [], "Can't get objects list")

        # reset methods
        self.fetcher.connect_to_db = original_connnect_to_db
        DbAccess.conn.cursor = original_cursor

    def test_get_objects_list_for_id_without_id_with_exception(self):
        mock_cursor = MockCursor(OBJECTS_LIST)
        # store original methods
        original_connnect_to_db = self.fetcher.connect_to_db
        original_cursor = DbAccess.conn.cursor

        # mock methods
        self.fetcher.connect_to_db = MagicMock()
        # mock exception
        DbAccess.conn.cursor = MagicMock(return_value=mock_cursor)
        mock_cursor.execute = MagicMock(side_effect=[AttributeError, ""])

        result = self.fetcher.get_objects_list_for_id(QUERY_WITHOUT_ID, OBJECT_TYPE, None)

        self.assertEqual(mock_cursor.execute.call_count, 2, "Can't invoke execute method twice when error occurs")
        self.assertNotEqual(result, [], "Can't get objects list")

        # reset methods
        self.fetcher.connect_to_db = original_connnect_to_db
        DbAccess.conn.cursor = original_cursor
