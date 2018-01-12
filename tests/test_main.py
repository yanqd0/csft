# -*- coding:utf-8 -*-

from os.path import curdir, devnull
from subprocess import check_call

from pytest import fixture, mark, raises

from csft import __main__ as main


@fixture
def null():
    with open(devnull, 'w') as fobj:
        yield fobj


def test_call(null):
    check_call(['python', '-m', 'csft', 'csft'], stdout=null, stderr=null)


@mark.parametrize('argv', [None, [], ['csft'], ])
def test_main(argv, mocker):
    obj = object()
    mocker.patch('sys.argv', ['csft'])
    csft2data = mocker.patch('csft.__main__.csft2data', return_value=obj)
    pr = mocker.patch('builtins.print')
    assert 0 == main.main(argv=argv)
    if argv:
        csft2data.assert_called_once_with(main._dir(argv[0]))
    else:
        csft2data.assert_called_once_with(main._dir(curdir))
    pr.assert_called_once_with(obj)


def test_wrong_path(capsys):
    with raises(SystemExit):
        main.main(argv=['path/is/not/a/directory'])
    assert capsys.readouterr()


def test_show_version(capsys):
    try:
        main.main(argv=['-V'])
    except SystemExit as err:
        assert 0 == err.code

    from csft import __version__
    out = capsys.readouterr()[0]
    assert __version__ == out.strip()
