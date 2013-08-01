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

    def test_signature_base_string(self):
        s = signing_requests.signature_base_string(
            http_method='GET',
            url='http://photos.example.net/photos',
            oauth_params=dict(
                oauth_consumer_key='dpf43f3p2l4k3l03',
                oauth_token='nnch734d00sl2jdk',
                oauth_signature_method='HMAC-SHA1',
                oauth_timestamp='1191242096',
                oauth_nonce='kllo9940pd9333jh',
                oauth_version='1.0'),
            get_params=dict(
                file='vacation.jpg',
                size='original'),
            post_params=dict())
        self.assertEqual(
            s,
            'GET&http%3A%2F%2Fphotos.example.net%2Fphotos&file%3Dvacation.jpg%'
            '26oauth_consumer_key%3Ddpf43f3p2l4k3l03%26oauth_nonce%3Dkllo9940p'
            'd9333jh%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D'
            '1191242096%26oauth_token%3Dnnch734d00sl2jdk%26oauth_version%3D1.0'
            '%26size%3Doriginal')
