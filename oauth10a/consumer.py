# used to obtain an unauthorized Request Token
request_token_url = None

# used to obtain User authorization for Consumer access
user_authorization_url = None

# used to exchange the User-authorized Request Token for an Access Token
access_token_url = None


def obtain_request_token():
    """OAuth 1.0a 6.1.1: Consumer Obtains a Request Token

    To obtain a Request Token, the Consumer sends an HTTP request to the
    Service Provider's Request Token URL. The Service Provider documentation
    specifies the HTTP method for this request, and HTTP POST is RECOMMENDED.
    The request MUST be signed and contains the following parameters:

    - `oauth_consumer_key`: The Consumer Key.
    - `oauth_signature_method`: The signature method the Consumer used to sign
      the request.
    - `oauth_signature`: The signature as defined in Signing Requests.
    - `oauth_timestamp`: As defined in Nonce and Timestamp.
    - `oauth_nonce`: As defined in Nonce and Timestamp.
    - `oauth_version`: OPTIONAL. If present, value MUST be 1.0 . Service
      Providers MUST assume the protocol version to be 1.0 if this parameter is
      not present.  Service Providers' response to non-1.0 value is left
      undefined.
    - `oauth_callback`: An absolute URL to which the Service Provider will
      redirect the User back when the Obtaining User Authorization step is
      completed. If the Consumer is unable to receive callbacks or a callback
      URL has been established via other means, the parameter value MUST be set
      to `oob` (case sensitive), to indicate an out-of-band configuration.

    - Additional parameters: Any additional parameters, as defined by the
      Service Provider.

    """
    pass


def direct_user_to_service_provider():
    """OAuth 1.0a 6.2.1: Consumer Directs the User to the Service Provider

    In order for the Consumer to be able to exchange the Request Token for an
    Access Token, the Consumer MUST obtain approval from the User by directing
    the User to the Service Provider. The Consumer constructs an HTTP GET
    request to the Service Provider's User Authorization URL with the following
    parameter:

    `oauth_token`: OPTIONAL. The Request Token obtained in the previous step.
    The Service Provider MAY declare this parameter as REQUIRED, or accept
    requests to the User Authorization URL without it, in which case it will
    prompt the User to enter it manually.

    Additional parameters: Any additional parameters, as defined by the Service
    Provider.

    Once the request URL has been constructed the Consumer redirects the User
    to the URL via the User's web browser. If the Consumer is incapable of
    automatic HTTP redirection, the Consumer SHALL notify the User how to
    manually go to the constructed request URL.

    Note: If a Service Provider knows a Consumer to be running on a mobile
    device or set-top box, the Service Provider SHOULD ensure that the User
    Authorization URL and Request Token are suitable for manual entry.

    """
    pass


def request_access_token():
    """6.3.1: Requests an Access Token

    The Request Token and Token Secret MUST be exchanged for an Access Token
    and Token Secret.

    To request an Access Token, the Consumer makes an HTTP request to the
    Service Provider's Access Token URL. The Service Provider documentation
    specifies the HTTP method for this request, and HTTP POST is RECOMMENDED.
    The request MUST be signed per Signing Requests, and contains the following
    parameters:

    - `oauth_consumer_key`: The Consumer Key.
    - `oauth_token`: The Request Token obtained previously.
    - `oauth_signature_method`: The signature method the Consumer used to sign
      the request.
    - `oauth_signature`: The signature as defined in Signing Requests.
    - `oauth_timestamp`: As defined in Nonce and Timestamp.
    - `oauth_nonce`: As defined in Nonce and Timestamp.
    - `oauth_version`: OPTIONAL. If present, value MUST be 1.0 . Service
      Providers MUST assume the protocol version to be 1.0 if this parameter is
      not present. Service Providers' response to non-1.0 value is left
      undefined.
    - `oauth_verifier`: The verification code received from the Service
      Provider in the Service Provider Directs the User Back to the Consumer
      step.

    No additional Service Provider specific parameters are allowed when
    requesting an Access Token to ensure all Token related information is
    present prior to seeking User approval.

    """
    pass


def access_protected_resource():
    """7: Accessing Protected Resources

    After successfully receiving the Access Token and Token Secret, the
    Consumer is able to access the Protected Resources on behalf of the User.
    The request MUST be signed per Signing Requests, and contains the following
    parameters:

    - `oauth_consumer_key`: The Consumer Key.
    - `oauth_token`: The Access Token.
    - `oauth_signature_method`: The signature method the Consumer used to sign
      the request.
    - `oauth_signature`: The signature as defined in Signing Requests.
    - `oauth_timestamp`: As defined in Nonce and Timestamp.
    - `oauth_nonce`: As defined in Nonce and Timestamp.
    - `oauth_version`: OPTIONAL. If present, value MUST be 1.0. Service
      Providers MUST assume the protocol version to be 1.0 if this parameter is
      not present. Service Providers' response to non-1.0 value is left
      undefined.
    - Additional parameters: Any additional parameters, as defined by the
      Service Provider.

    """
    pass
