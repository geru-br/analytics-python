
from celery import shared_task

from geru.ccdf import track as actual_track
from geru.ccdf import identify as actual_identify
from geru.ccdf import group as actual_group
from geru.ccdf import alias as actual_alias
from geru.ccdf import page as actual_page
from geru.ccdf import screen as actual_screen
from geru.ccdf import join as actual_flush
from geru.ccdf import join as actual_join


@shared_task(bind=True, queue='geru.ccdf')
def track(self, *args, **kwargs):
    """Send a track call."""
    actual_track(*args, **kwargs)


@shared_task(bind=True, queue='geru.ccdf')
def identify(*args, **kwargs):
    """Send a identify call."""
    actual_identify(*args, **kwargs)


@shared_task(bind=True, queue='geru.ccdf')
def group(*args, **kwargs):
    """Send a group call."""
    actual_group(*args, **kwargs)


@shared_task(bind=True, queue='geru.ccdf')
def alias(*args, **kwargs):
    """Send a alias call."""
    actual_alias(*args, **kwargs)


@shared_task(bind=True, queue='geru.ccdf')
def page(*args, **kwargs):
    """Send a page call."""
    actual_page(*args, **kwargs)


@shared_task(bind=True, queue='geru.ccdf')
def screen(*args, **kwargs):
    """Send a screen call."""
    actual_screen(*args, **kwargs)


@shared_task(bind=True, queue='geru.ccdf')
def flush():
    """Tell the client to flush."""
    actual_flush()


@shared_task(bind=True, queue='geru.ccdf')
def join():
    """Block program until the client clears the queue."""
    actual_join()
