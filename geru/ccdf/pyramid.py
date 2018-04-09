"""Use pyramid configuration to configure client"""


def includeme(settings):

    import geru.ccdf
    geru.ccdf.write_key = settings.get_settings().get('geru.ccdf.write_key')
    geru.ccdf.host = settings.get_settings().get('geru.ccdf.host')
    geru.ccdf.debug = settings.get_settings().get('geru.ccdf.debug')
