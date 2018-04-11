import pytest


@pytest.fixture()
def celery_config():
    return {
        'broker_url': 'redis://localhost/6',
        'result_backend': 'redis://localhost/7',
        #'task_ignore_result': True,
        'task_always_eager': True,
    }


@pytest.fixture()
def celery_includes():
    return [
        'geru.ccdf.tasks',
    ]


@pytest.fixture(scope='session')
def celery_enable_logging():
    return True
