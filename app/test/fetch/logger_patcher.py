import unittest
from unittest.mock import patch


class LoggerPatcher(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.logger_patcher = patch(
            'discover.fetcher.FullLogger'
        )
        self.logger_class = self.logger_patcher.start()

    def tearDown(self):
        self.logger_patcher.stop()
        super().tearDown()
