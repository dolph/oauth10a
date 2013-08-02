from oauth10a import consumer

from tests import test_oauth10a


class TestCase(test_oauth10a.TestCase):
    def test_trivial(self):
        self.assertTrue(consumer)

    def test_termie(self):
        request_token_url = 'http://term.ie/oauth/example/request_token.php'
        consumer_key = 'key'
        consumer_secret = 'secret'

        r = consumer.obtain_request_token(
            request_token_url,
            consumer_key,
            consumer_secret,
            http_method='GET')
        self.assertEqual(
            r.text, 'oauth_token=requestkey&oauth_token_secret=requestsecret')
