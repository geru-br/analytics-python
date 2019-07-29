

def test_pyramid_integration():
    import geru.ccdf
    from pyramid.config import Configurator

    assert geru.ccdf.write_key is None
    assert geru.ccdf.host is None
    assert geru.ccdf.debug == False
    assert geru.ccdf.testing == False

    with Configurator(settings={
        'geru.ccdf.write_key': 'A write key',
        'geru.ccdf.host': 'a-host.example.com',
        'geru.ccdf.debug': 'false',
        'geru.ccdf.testing': 'true',
    }) as config:
        config.include('geru.ccdf.pyramid')

        assert geru.ccdf.write_key == 'A write key'
        assert geru.ccdf.host == 'a-host.example.com'
        assert geru.ccdf.debug == False
        assert geru.ccdf.testing == True
