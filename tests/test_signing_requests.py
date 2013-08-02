import urlparse

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


class LinkedInTestCase(test_oauth10a.TestCase):
    def setUp(self):
        # http://developer.linkedin.com/oauth-test-console
        self.consumer_key = 'efubm7z8ww6k40m9l5czq25l0'
        self.consumer_secret = '1ln2puav04fl6s22oy0l98x69'
        self.member_token = 'akk4fj6h5967zc0ra6hzmsd62'
        self.member_secret = 'amppgl8vnr7hgaqqzi0igoq4f'
        self.http_verb = 'GET'
        self.url = 'http://example.com/8szrt134wyc0e8kdqwxj3bmf'
        self.query_params = '5268cf=4rbjsn&a7xbsd=7h0qfi'
        self.nonce = 'mjylxo54rrqad1fjxjhf67cc'
        self.timestamp = 1375241716

        self.expected_signature_base_string = (
            'GET&http%3A%2F%2Fexample.com%2F8szrt134wyc0e8kdqwxj3bmf&5268cf%3D'
            '4rbjsn%26a7xbsd%3D7h0qfi%26oauth_consumer_key%3Defubm7z8ww6k40m9l'
            '5czq25l0%26oauth_nonce%3Dmjylxo54rrqad1fjxjhf67cc%26oauth_signatu'
            're_method%3DHMAC-SHA1%26oauth_timestamp%3D1375241716%26oauth_toke'
            'n%3Dakk4fj6h5967zc0ra6hzmsd62%26oauth_version%3D1.0')
        self.expected_signature = 'Ilt9SqALMiI9fwmgrNv+JzICEF4='
        self.expected_http_authentication_header = (
            'OAuth oauth_nonce="mjylxo54rrqad1fjxjhf67cc" oauth_timestamp="137'
            '5241716" oauth_version="1.0" oauth_signature_method="HMAC-SHA1" o'
            'auth_consumer_key="efubm7z8ww6k40m9l5czq25l0" oauth_token="akk4fj'
            '6h5967zc0ra6hzmsd62" oauth_signature="Ilt9SqALMiI9fwmgrNv%2BJzICE'
            'F4%3D"')
        self.expected_url = 'http://example.com/8szrt134wyc0e8kdqwxj3bmf'

    def test_request_url(self):
        url = self.url
        request_url = signing_requests.request_url(url)
        self.assertEqual(request_url, self.expected_url)

    def test_signature_base_string(self):
        s = signing_requests.signature_base_string(
            http_method=self.http_verb,
            url=self.url,
            oauth_params=dict(
                oauth_consumer_key=self.consumer_key,
                oauth_token=self.member_token,
                oauth_signature_method='HMAC-SHA1',
                oauth_timestamp=str(self.timestamp),
                oauth_nonce=self.nonce,
                oauth_version='1.0'),
            get_params=dict(urlparse.parse_qsl(self.query_params)))
        self.assertEqual(s, self.expected_signature_base_string)
