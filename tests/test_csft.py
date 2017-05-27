# -*- coding:utf-8 -*-
from os.path import dirname

from pandas import DataFrame
from csft import csft


def test_file_type():
    assert '.py' == csft.type_of_file(__file__)
    assert '' == csft.type_of_file('no_ext')


def test_type_size_data():
    test_dir = dirname(__file__)
    data = csft.csft2data(test_dir)
    assert isinstance(data, DataFrame)
    assert data['type'].str.contains('py').sum()
