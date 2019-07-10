"""Use pyramid configuration to configure client"""

from pyramid.settings import asbool


def includeme(settings):
    import geru.ccdf
    geru.ccdf.write_key = settings.get_settings().get('geru.ccdf.write_key')
    geru.ccdf.host = settings.get_settings().get('geru.ccdf.host')
    geru.ccdf.debug = asbool(settings.get_settings().get('geru.ccdf.debug'))

    geru.ccdf.testing = asbool(settings.get_settings().get('geru.ccdf.testing'))
