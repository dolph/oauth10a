def issue_unauthorized_request_token():
    """6.1.2: Issues an Unauthorized Request Token

    The Service Provider verifies the signature and Consumer Key. If
    successful, it generates a Request Token and Token Secret and returns them
    to the Consumer in the HTTP response body as defined in Service Provider
    Response Parameters. The Service Provider MUST ensure the Request Token
    cannot be exchanged for an Access Token until the User successfully grants
    access in Obtaining User Authorization.

    The response contains the following parameters:

    - `oauth_token`: The Request Token.
    - `oauth_token_secret`: The Token Secret.
    - `oauth_callback_confirmed`: MUST be present and set to true. The Consumer
      MAY use this to confirm that the Service Provider received the callback
      value.

    - Additional parameters: Any additional parameters, as defined by the
      Service Provider. If the request fails verification or is rejected for
      other reasons, the Service Provider SHOULD respond with the appropriate
      response code as defined in HTTP Response Codes. The Service Provider MAY
      include some further details about why the request was rejected in the
      HTTP response body as defined in Service Provider Response Parameters.

    """
    pass


def authenticate_user_and_obtain_consent():
    """6.2.2: Authenticates the User and Obtains Consent

    The Service Provider verifies the User's identity and asks for consent as
    detailed. OAuth does not specify how the Service Provider authenticates the
    User. However, it does define a set of REQUIRED steps:

    - The Service Provider MUST first verify the User's identity before asking
      for consent. It MAY prompt the User to sign in if the User has not
      already done so.

    - The Service Provider presents to the User information about the Consumer
      requesting access (as registered by the Consumer Developer). The
      information includes the duration of the access and the Protected
      Resources provided. The information MAY include other details specific to
      the Service Provider.

    - The User MUST grant or deny permission for the Service Provider to give
      the Consumer access to the Protected Resources on behalf of the User. If
      the User denies the Consumer access, the Service Provider MUST NOT allow
      access to the Protected Resources.

    When displaying any identifying information about the Consumer to the User
    based on the Consumer Key, the Service Provider MUST inform the User if it
    is unable to assure the Consumer's true identity. The method in which the
    Service Provider informs the User and the quality of the identity assurance
    is beyond the scope of this specification.

    """
    pass


def direct_user_back_to_consumer():
    """6.2.3: Directs the User Back to the Consumer

    After the User authenticates with the Service Provider and grants
    permission for Consumer access, the Consumer MUST be notified that the
    Request Token has been authorized and ready to be exchanged for an Access
    Token. If the User denies access, the Consumer MAY be notified that the
    Request Token has been revoked.

    To make sure that the User granting access is the same User returning back
    to the Consumer to complete the process, the Service Provider MUST generate
    a verification code: an unguessable value passed to the Consumer via the
    User and REQUIRED to complete the process.

    If the Consumer provided a callback URL (using the oauth_callback parameter
    in Section 6.1.1 or by other means), the Service Provider uses it to
    constructs an HTTP request, and directs the User's web browser to that URL
    with the following parameters added:

    - `oauth_token`: The Request Token the User authorized or denied.
    - `oauth_verifier`: The verification code.

    The callback URL MAY include Consumer provided query parameters. The
    Service Provider MUST retain them unmodified and append the OAuth
    parameters to the existing query.

    If the Consumer did not provide a callback URL, the Service Provider SHOULD
    display the value of the verification code, and instruct the User to
    manually inform the Consumer that authorization is completed. If the
    Service Provider knows a Consumer to be running on a mobile device or
    set-top box, the Service Provider SHOULD ensure that the verifier value is
    suitable for manual entry.

    """
    pass


def grant_access_token():
    """6.3.2: Grants an Access Token

    The Service Provider MUST ensure that:

    - The request signature has been successfully verified.
    - The Request Token has never been exchanged for an Access Token.
    - The Request Token matches the Consumer Key.
    - The verification code received from the Consumer has been successfully
      verified.

    If successful, the Service Provider generates an Access Token and Token
    Secret and returns them in the HTTP response body as defined in Service
    Provider Response Parameters. The Access Token and Token Secret are stored
    by the Consumer and used when signing Protected Resources requests. The
    response contains the following parameters:

    - `oauth_token`: The Access Token.
    - `oauth_token_secret`: The Token Secret.
    - Additional parameters: Any additional parameters, as defined by the
      Service Provider.

    If the request fails verification or is rejected for other reasons, the
    Service Provider SHOULD respond with the appropriate response code as
    defined in HTTP Response Codes. The Service Provider MAY include some
    further details about why the request was rejected in the HTTP response
    body as defined in Service Provider Response Parameters.

    """
    pass
