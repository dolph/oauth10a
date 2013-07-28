from oauth10a import consumer

from tests import test_oauth10a


class TestCase(test_oauth10a.TestCase):
    def test_trivial(self):
        self.assertTrue(consumer)
