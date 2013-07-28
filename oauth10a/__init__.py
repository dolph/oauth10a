"""OAuth Core 1.0 Revision A

This implementation and the included documentation were derived from the Oauth
Core 1.0 Revision A specification available at http://oauth.net/core/1.0a/

The OAuth protocol enables websites or applications (Consumers) to access
Protected Resources from a web service (Service Provider) via an API, without
requiring Users to disclose their Service Provider credentials to the
Consumers. More generally, OAuth creates a freely-implementable and generic
methodology for API authentication.

An example use case is allowing printing service printer.example.com (the
Consumer), to access private photos stored on photos.example.net (the Service
Provider) without requiring Users to provide their photos.example.net
credentials to printer.example.com.

OAuth does not require a specific user interface or interaction pattern, nor
does it specify how Service Providers authenticate Users, making the protocol
ideally suited for cases where authentication credentials are unavailable to
the Consumer, such as with OpenID.

OAuth aims to unify the experience and implementation of delegated web service
authentication into a single, community-driven protocol. OAuth builds on
existing protocols and best practices that have been independently implemented
by various websites. An open standard, supported by large and small providers
alike, promotes a consistent and trusted experience for both application
developers and the users of those applications.

Definitions:

- Service Provider: A web application that allows access via OAuth.

- User: An individual who has an account with the Service Provider.

- Consumer: A website or application that uses OAuth to access the Service
  Provider on behalf of the User.

- Protected Resource(s): Data controlled by the Service Provider, which the
  Consumer can access through authentication.

- Consumer Developer: An individual or organization that implements a Consumer.

- Consumer Key: A value used by the Consumer to identify itself to the Service
  Provider.

- Consumer Secret: A secret used by the Consumer to establish ownership of the
  Consumer Key.

- Request Token: A value used by the Consumer to obtain authorization from the
  User, and exchanged for an Access Token.

- Access Token: A value used by the Consumer to gain access to the Protected
  Resources on behalf of the User, instead of using the User's Service Provider
  credentials.

- Token Secret: A secret used by the Consumer to establish ownership of a given
  Token.

- OAuth Protocol Parameters: Parameters with names beginning with oauth_.

OAuth includes a Consumer Key and matching Consumer Secret that together
authenticate the Consumer (as opposed to the User) to the Service Provider.
Consumer-specific identification allows the Service Provider to vary access
levels to Consumers (such as un-throttled access to resources).

Service Providers SHOULD NOT rely on the Consumer Secret as a method to verify
the Consumer identity, unless the Consumer Secret is known to be inaccessible
to anyone other than the Consumer and the Service Provider. The Consumer Secret
MAY be an empty string (for example when no Consumer verification is needed, or
when verification is achieved through other means such as RSA).

"""
