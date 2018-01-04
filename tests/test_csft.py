# -*- coding:utf-8 -*-
from os.path import dirname

from pandas import DataFrame
from csft import _csft


def test_file_type():
    assert '.py' == _csft.type_of_file(__file__)
    assert '' == _csft.type_of_file('no_ext')


def test_type_size_data():
    test_dir = dirname(__file__)
    data = _csft.csft2data(test_dir)
    assert isinstance(data, DataFrame)
    assert data['type'].str.contains('py').sum()
