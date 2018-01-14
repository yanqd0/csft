from pytest import fixture, mark

import csft


def test_meta():
    assert csft.__author__
    assert csft.__version__
    assert csft.__email__
    assert csft.__url__
    assert csft.__copyright__
    assert csft.__license__


@fixture
def mock_pkg_resources():
    import sys
    bak = sys.modules['pkg_resources']
    sys.modules['pkg_resources'] = __import__('mock')
    yield bak
    sys.modules['pkg_resources'] = bak


@mark.usefixtures(mock_pkg_resources.__name__)
def test_get_version_import_error():
    assert 'x.x.x.dev' == csft._get_version()

    default = 'xxx'
    assert default == csft._get_version(default=default)


def test_get_version_distribution_not_found(mocker):
    from pkg_resources import DistributionNotFound
    dist = mocker.patch('pkg_resources.get_distribution')
    dist.side_effect = DistributionNotFound
    assert 'x.x.x.dev' == csft._get_version()
    dist.assert_called_once()
