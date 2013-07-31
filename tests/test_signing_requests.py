from oauth10a import signing_requests

from tests import test_oauth10a


class TestCase(test_oauth10a.TestCase):
    def test_trivial(self):
        self.assertTrue(signing_requests)

    def test_request_url(self):
        url = 'HTTP://Example.com:80/resource?id=123'
        request_url = signing_requests.request_url(url)
        self.assertEqual(request_url, 'http://example.com/resource')

    def test_normalized_request_parameters(self):
        normalized = signing_requests.normalized_request_parameters(
            oauth_params=dict(a=1, c='hi%20there', f=25, z='p'),
            get_params=dict(f=50, z='t'),
            post_params=dict(f='a'))
        self.assertEqual(normalized, 'a=1&c=hi%20there&f=25&f=50&f=a&z=p&z=t')

    def test_normalized_request_parameters_excludes_oauth_signature(self):
        normalized = signing_requests.normalized_request_parameters(
            oauth_params=dict(
                oauth_consumer_key='dpf43f3p2l4k3l03',
                oauth_token='nnch734d00sl2jdk',
                oauth_signature_method='HMAC-SHA1',
                oauth_signature='pending',
                oauth_timestamp='1191242096',
                oauth_nonce='kllo9940pd9333jh',
                oauth_version='1.0'),
            get_params=dict(
                file='vacation.jpg',
                size='original'),
            post_params=dict())
        self.assertEqual(
            normalized,
            'file=vacation.jpg&oauth_consumer_key=dpf43f3p2l4k3l03&oauth_nonce'
            '=kllo9940pd9333jh&oauth_signature_method=HMAC-SHA1&oauth_timestam'
            'p=1191242096&oauth_token=nnch734d00sl2jdk&oauth_version=1.0&size='
            'original')
