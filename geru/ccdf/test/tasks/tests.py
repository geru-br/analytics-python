

def setup_module(module):
    import geru
    import geru.ccdf.tasks
    geru.ccdf.write_key = 'testsecret'


def test_track(celery_worker):
    from geru.ccdf.tasks import track
    track.delay('userId', 'python module event')


def test_identify(celery_worker):
    from geru.ccdf.tasks import identify
    identify.delay('userId', {'email': 'user@email.com'})


def test_group(celery_worker):
    from geru.ccdf.tasks import group
    group.delay('userId', 'groupId')


def test_alias(celery_worker):
    from geru.ccdf.tasks import alias
    alias.delay('previousId', 'userId')


def test_page(celery_worker):
    from geru.ccdf.tasks import page
    page.delay('userId')


def test_screen(celery_worker):
    from geru.ccdf.tasks import screen
    screen.delay('userId')
