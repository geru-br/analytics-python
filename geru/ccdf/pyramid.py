"""Use pyramid configuration to configure client"""

from pyramid.settings import asbool


def includeme(config):
    import geru.ccdf
    geru.ccdf.write_key = config.get_settings().get('geru.ccdf.write_key')
    geru.ccdf.host = config.get_settings().get('geru.ccdf.host')
    geru.ccdf.debug = asbool(config.get_settings().get('geru.ccdf.debug'))

    geru.ccdf.testing = asbool(config.get_settings().get('geru.ccdf.testing'))
