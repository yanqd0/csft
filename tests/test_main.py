# -*- coding:utf-8 -*-

import sys
from subprocess import check_call

from pytest import raises

import csft
from csft import __main__ as main


def test_call():
    check_call(['python', '-m', 'csft', '.'])


def test_main():
    assert 0 == main.main(argv=['.'])


def test_wrong_path():
    with raises(SystemExit):
        main.main(argv=[])

    with raises(SystemExit):
        main.main(argv=['path/is/not/a/directory'])


class _Buffer(object):
    def __init__(self):
        self.buffer = []

    def write(self, text):
        self.buffer.append(text)


def test_show_version():
    test_buf = _Buffer()
    if sys.version < '3.0':
        test_buf, sys.stderr = sys.stderr, test_buf
    else:
        test_buf, sys.stdout = sys.stdout, test_buf

    try:
        main.main(argv=['-V'])
    except SystemExit as err:
        assert 0 == err.code
    finally:
        if sys.version < '3.0':
            test_buf, sys.stderr = sys.stderr, test_buf
        else:
            test_buf, sys.stdout = sys.stdout, test_buf

    assert test_buf.buffer[0].strip() == csft.__version__
