# -*- coding:utf-8 -*-

from os.path import devnull
from subprocess import check_call

from pytest import fixture, raises

from csft import __main__ as main


@fixture
def null():
    with open(devnull, 'w') as fobj:
        yield fobj


def test_call(null):
    check_call(['python', '-m', 'csft', 'csft'], stdout=null, stderr=null)


def test_main(mocker):
    obj = object()
    csft2data = mocker.patch('csft.__main__.csft2data', return_value=obj)
    pr = mocker.patch('builtins.print')
    assert 0 == main.main(argv=['csft'])
    csft2data.assert_called_once_with(main._dir('csft'))
    pr.assert_called_once_with(obj)


def test_wrong_path(capsys):
    with raises(SystemExit):
        main.main(argv=[])
    assert capsys.readouterr()

    with raises(SystemExit):
        main.main(argv=['path/is/not/a/directory'])
    assert capsys.readouterr()


def test_show_version(capsys):
    try:
        main.main(argv=['-V'])
    except SystemExit as err:
        assert 0 == err.code

    from csft import __version__
    assert __version__ == capsys.readouterr().out.strip()
