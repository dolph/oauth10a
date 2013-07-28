from oauth10a import utils

from tests import test_oauth10a


class TestCase(test_oauth10a.TestCase):
    def test_nonce(self):
        nonce = utils.nonce()
        self.assertIsInstance(nonce, basestring)
        self.assertTrue(nonce)

    def test_timestamp(self):
        timestamp = utils.timestamp()
        self.assertIsInstance(timestamp, int)
        self.assertTrue(timestamp > 0)
