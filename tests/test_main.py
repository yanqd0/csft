# -*- coding:utf-8 -*-

import sys
from os.path import curdir, devnull
from subprocess import check_call

from pandas import DataFrame
from pytest import fixture, mark, raises

from csft import __main__ as main


@fixture
def null():
    with open(devnull, 'w') as fobj:
        yield fobj


def test_call(null):
    check_call(['python', '-m', 'csft', 'csft'], stdout=null, stderr=null)


@mark.parametrize('argv', [None, [], ['csft'], ])
def test_main(argv, mocker, capsys):
    expect = 'TEST_PRINT'
    mocker.patch('sys.argv', ['csft'])
    csft2data = mocker.patch('csft.__main__.csft2data', return_value=expect)

    assert 0 == main.main(argv=argv)

    if argv:
        csft2data.assert_called_once_with(main._dir(argv[0]))
    else:
        csft2data.assert_called_once_with(main._dir(curdir))

    assert expect == capsys.readouterr()[0].strip()


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
    if sys.version < '3.0':
        out = capsys.readouterr()[1]
    else:
        out = capsys.readouterr()[0]
    assert __version__ == out.strip()


def test_arg_top(mocker, capsys):
    expect = 'TEST_PRINT'
    obj = DataFrame()
    mocker.patch.object(obj, 'head', return_value=expect)
    csft2data = mocker.patch('csft.__main__.csft2data', return_value=obj)

    assert 0 == main.main(argv=[curdir, '--top', '5'])
    csft2data.assert_called_once_with(main._dir(curdir))
    assert expect == capsys.readouterr()[0].strip()

    with raises(SystemExit):
        main.main(argv=[curdir, '--top', 'not-a-number'])
    with raises(SystemExit):
        main.main(argv=[curdir, '--top', '-1'])
