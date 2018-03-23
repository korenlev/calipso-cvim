from unittest.mock import patch

from test.test_base import TestBase


class LoggerPatcher(TestBase):

    def setUp(self):
        super().setUp()

        self.logger_patcher = patch(
            'discover.fetcher.FullLogger'
        )
        self.logger_class = self.logger_patcher.start()

    def tearDown(self):
        self.logger_patcher.stop()
        super().tearDown()
