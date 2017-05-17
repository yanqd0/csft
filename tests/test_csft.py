# -*- coding:utf-8 -*-
from os.path import dirname

from csft import csft


def test_file_type():
    assert '.py' == csft.type_of_file(__file__)
    assert '' == csft.type_of_file('no_ext')


def test_print_result():
    test_dir = dirname(__file__)
    status = csft.print_result(test_dir)
    assert isinstance(status, int)
    assert status == 0
