
from geru.ccdf.client import Client
from geru.ccdf.utils import testing_log


__version__ = '0.0.3'

"""Settings."""
write_key = None
host = None
on_error = None
debug = False
testing = False
send = True

default_client = None



def track(*args, **kwargs):
    """Send a track call."""
    _proxy('track', *args, **kwargs)


def identify(*args, **kwargs):
    """Send a identify call."""
    _proxy('identify', *args, **kwargs)


def group(*args, **kwargs):
    """Send a group call."""
    _proxy('group', *args, **kwargs)


def alias(*args, **kwargs):
    """Send a alias call."""
    _proxy('alias', *args, **kwargs)


def page(*args, **kwargs):
    """Send a page call."""
    _proxy('page', *args, **kwargs)


def screen(*args, **kwargs):
    """Send a screen call."""
    _proxy('screen', *args, **kwargs)


def flush():
    """Tell the client to flush."""
    _proxy('flush')


def join():
    """Block program until the client clears the queue"""
    _proxy('join')


def _proxy(*args, **kwargs):
    if testing:
        return _testing_proxy(*args, **kwargs)

    else:
        return _client_proxy(*args, **kwargs)


def _client_proxy(method, *args, **kwargs):
    """Create an analytics client if one doesn't exist and send to it."""
    global default_client
    if not default_client:
        default_client = Client(write_key, host=host, debug=debug, on_error=on_error,
                                send=send)

    fn = getattr(default_client, method)
    fn(*args, **kwargs)


def _testing_proxy(method, *args, **kwargs):
    """Save analytics data to log instead of analytics client."""
    testing_log.debug("%s, %r, %r", method, args, kwargs)
