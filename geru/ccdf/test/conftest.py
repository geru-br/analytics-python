import pytest


@pytest.fixture(autouse=True)
def geru_ccdf_config_cleanup():
    """ Force clean up module level config after every test.

    Some tests have been polluting geru.ccdf settings and not restoring
    afterwards.

    So we just clean up after each of them.
    """
    import geru.ccdf
    backup = geru.ccdf.__dict__.copy()

    yield geru.ccdf
    # restore backup:
    geru.ccdf.__dict__.update(backup)
