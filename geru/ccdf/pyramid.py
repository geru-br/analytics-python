"""Use pyramid configuration to configure client"""
from __future__ import absolute_import
# This file is called `pyramid.py` but is trying to import from a global
# pyramid package below, so we need absolute imports above on Python 2

from pyramid.settings import asbool


def includeme(config):
    import geru.ccdf
    geru.ccdf.write_key = config.get_settings().get('geru.ccdf.write_key')
    geru.ccdf.host = config.get_settings().get('geru.ccdf.host')
    geru.ccdf.debug = asbool(config.get_settings().get('geru.ccdf.debug'))

    geru.ccdf.testing = asbool(config.get_settings().get('geru.ccdf.testing'))
