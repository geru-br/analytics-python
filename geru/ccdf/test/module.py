import unittest

import geru.ccdf


class TestModule(unittest.TestCase):

    def failed(self):
        self.failed = True

    def setUp(self):
        self.failed = False
        geru.ccdf.write_key = 'testsecret'
        geru.ccdf.on_error = self.failed

    def test_no_write_key(self):
        geru.ccdf.write_key = None
        self.assertRaises(Exception, geru.ccdf.track)

    def test_no_host(self):
        geru.ccdf.host = None
        self.assertRaises(Exception, geru.ccdf.track)

    def test_track(self):
        geru.ccdf.track('userId', 'python module event')
        geru.ccdf.flush()

    def test_identify(self):
        geru.ccdf.identify('userId', { 'email': 'user@email.com' })
        geru.ccdf.flush()

    def test_group(self):
        geru.ccdf.group('userId', 'groupId')
        geru.ccdf.flush()

    def test_alias(self):
        geru.ccdf.alias('previousId', 'userId')
        geru.ccdf.flush()

    def test_page(self):
        geru.ccdf.page('userId')
        geru.ccdf.flush()

    def test_screen(self):
        geru.ccdf.screen('userId')
        geru.ccdf.flush()

    def test_flush(self):
        geru.ccdf.flush()
