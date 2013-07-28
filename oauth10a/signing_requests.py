"""
All Token requests and Protected Resources requests MUST be signed by the
Consumer and verified by the Service Provider. The purpose of signing requests
is to prevent unauthorized parties from using the Consumer Key and Tokens when
making Token requests or Protected Resources requests. The signature process
encodes the Consumer Secret and Token Secret into a verifiable value which is
included with the request.

OAuth does not mandate a particular signature method, as each implementation
can have its own unique requirements. The protocol defines three signature
methods: HMAC-SHA1, RSA-SHA1, and PLAINTEXT, but Service Providers are free to
implement and document their own methods. Recommending any particular method is
beyond the scope of this specification.

The Consumer declares a signature method in the oauth_signature_method
parameter, generates a signature, and stores it in the oauth_signature
parameter. The Service Provider verifies the signature as specified in each
method. When verifying a Consumer signature, the Service Provider SHOULD check
the request nonce to ensure it has not been used in a previous Consumer
request.

The signature process MUST NOT change the request parameter names or values,
with the exception of the oauth_signature parameter.

"""

import requests


class AuthBase(requests.auth.AuthBase):
    @property
    def signature_base_string(self):
        """Consistent reproducible concatenation of the request elements.

        The string is used as an input in hashing or signing algorithms.

        """
        pass

    @property
    def normalized_request_parameters(self):
        """The request parameters are collected, sorted and concatenated into a
        normalized string:

        - Parameters in the OAuth HTTP Authorization header excluding the realm
          parameter.
        - Parameters in the HTTP POST request body (with a content-type of
          application/x-www-form-urlencoded).
        - HTTP GET parameters added to the URLs in the query part (as defined
          by [RFC3986] section 3).

        The oauth_signature parameter MUST be excluded.

        The parameters are normalized into a single string as follows:

        Parameters are sorted by name, using lexicographical byte value
        ordering. If two or more parameters share the same name, they are
        sorted by their value. For example:

            a=1, c=hi%20there, f=25, f=50, f=a, z=p, z=t

        Parameters are concatenated in their sorted order into a single string.
        For each parameter, the name is separated from the corresponding value
        by an '=' character (ASCII code 61), even if the value is empty. Each
        name-value pair is separated by an '&' character (ASCII code 38). For
        example:

            a=1&c=hi%20there&f=25&f=50&f=a&z=p&z=t

        """
        pass

    @property
    def request_url(self):
        """9.1.2: Construct Request URL

        The Signature Base String includes the request absolute URL, tying the
        signature to a specific endpoint. The URL used in the Signature Base
        String MUST include the scheme, authority, and path, and MUST exclude
        the query and fragment as defined by [RFC3986] section 3.

        If the absolute request URL is not available to the Service Provider
        (it is always available to the Consumer), it can be constructed by
        combining the scheme being used, the HTTP Host header, and the relative
        HTTP request URL. If the Host header is not available, the Service
        Provider SHOULD use the host name communicated to the Consumer in the
        documentation or other means.

        The Service Provider SHOULD document the form of URL used in the
        Signature Base String to avoid ambiguity due to URL normalization.
        Unless specified, URL scheme and authority MUST be lowercase and
        include the port number; http default port 80 and https default port
        443 MUST be excluded.

        For example, the request:

            HTTP://Example.com:80/resource?id=123

        Is included in the Signature Base String as:

            http://example.com/resource

        """
        pass

    @property
    def request_elements(self):
        """9.1.3: Concatenate Request Elements

        The following items MUST be concatenated in order into a single string.
        Each item is encoded and separated by an '&' character (ASCII code 38),
        even if empty.

        - The HTTP request method used to send the request. Value MUST be
          uppercase, for example: HEAD, GET , POST, etc.
        - The request URL from Section 9.1.2.
        - The normalized request parameters string from Section 9.1.1.

        See Signature Base String example in Appendix A.5.1.

        """
        pass


class HMACSHA1Auth(AuthBase):
    """9.2: HMAC-SHA1

    The HMAC-SHA1 signature method uses the HMAC-SHA1 signature algorithm as
    defined in [RFC2104] where the Signature Base String is the text and the
    key is the concatenated values (each first encoded per Parameter Encoding)
    of the Consumer Secret and Token Secret, separated by an '&' character
    (ASCII code 38) even if empty.

    """
    def __init__(self):
        pass

    def __call__(self, r):
        """9.2.1: Generating Signature

        `oauth_signature` is set to the calculated digest octet string, first
        base64-encoded per [RFC2045] section 6.8, then URL-encoded per
        Parameter Encoding.

        """
        oauth_signature = self.generate_signature()
        return r


class RSASHA1Auth(AuthBase):
    def __init__(self):
        pass

    def __call__(self, r):
        """9.3.1: Generating Signature

        The Signature Base String is signed using the Consumer's RSA private
        key per [RFC3447] section 8.2.1, where K is the Consumer's RSA private
        key, M the Signature Base String, and S is the result signature octet
        string:

            S = RSASSA-PKCS1-V1_5-SIGN (K, M)

        oauth_signature is set to S, first base64-encoded per [RFC2045] section
        6.8, then URL-encoded per Parameter Encoding.

        """
        return r


class PlaintextAuth(AuthBase):
    """9.4: Plaintext

    The PLAINTEXT method does not provide any security protection and SHOULD
    only be used over a secure channel such as HTTPS. It does not use the
    Signature Base String.

    """

    def __init__(self):
        pass

    def __call__(self, r):
        """9.4.1: Generating Signature

        `oauth_signature` is set to the concatenated encoded values of the
        Consumer Secret and Token Secret, separated by a '&' character (ASCII
        code 38), even if either secret is empty. The result MUST be encoded
        again.

        These examples show the value of `oauth_signature` for Consumer Secret
        `djr9rjt0jd78jf88` and 3 different Token Secrets:

        jjd999tj88uiths3:

            oauth_signature=djr9rjt0jd78jf88%26jjd999tj88uiths3

        jjd99$tj88uiths3:

            oauth_signature=djr9rjt0jd78jf88%26jjd99%2524tj88uiths3

        Empty:

            oauth_signature=djr9rjt0jd78jf88%26

        """
        return r
