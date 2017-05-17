# -*- coding:utf-8 -*-

from subprocess import check_call

from pytest import raises

from csft import __main__ as main


def test_call():
    check_call(['python', '-m', 'csft', '.'])


def test_main():
    main.main(argv=['.'])

    with raises(SystemExit):
        main.main(argv=[])
