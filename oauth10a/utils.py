import time
import uuid


def nonce():
    """Produces a random string.

        >>> nonce()
        'e1a2d5c1b59e4d2cbf25988785148745'

    """
    return uuid.uuid4().hex


def timestamp():
    """Returns the number of seconds since January 1, 1970 00:00:00 GMT.

        >>> timestamp()
        1375011657

    """
    return int(time.mktime(time.gmtime()))
