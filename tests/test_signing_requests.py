from oauth10a import signing_requests

from tests import test_oauth10a


class TestCase(test_oauth10a.TestCase):
    def test_trivial(self):
        self.assertTrue(signing_requests)

    def test_request_url(self):
        url = 'HTTP://Example.com:80/resource?id=123'
        request_url = signing_requests.request_url(url)
        self.assertEqual(request_url, 'http://example.com/resource')
