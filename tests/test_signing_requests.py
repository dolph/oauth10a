from oauth10a import signing_requests

from tests import test_oauth10a


class TestCase(test_oauth10a.TestCase):
    def test_trivial(self):
        self.assertTrue(signing_requests)
