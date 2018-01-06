# -*- coding:utf-8 -*-
from collections import Iterable
from os.path import dirname, isfile, join

from pandas import DataFrame, Series
from pytest import fixture

from csft import _csft
from csft._csft import column


def test_file_type():
    assert '.py' == _csft.type_of_file(__file__)
    assert '' == _csft.type_of_file('no_ext')


@fixture(scope='module')
def tempdir():
    import tempfile
    import shutil

    temp = tempfile.mkdtemp()
    shutil.copytree('csft', join(temp, 'csft'))
    shutil.copy('LICENSE', temp)
    shutil.copy('requirements.txt', temp)
    yield temp

    shutil.rmtree(temp)


def test_make_file_list(tempdir):
    files = _csft.make_file_list(tempdir)
    assert len(files) >= 5
    assert isinstance(files, Iterable)
    assert all(isfile(f) for f in files)


def test_make_raw_data(mocker):
    paths = ['file.a', 'file.b', 'file.c']
    mocker.patch('csft._csft.getsize', lambda path: paths.index(path))

    data = _csft.make_raw_data(paths)

    assert isinstance(data, DataFrame)
    assert all(data.get(column.PATH) == Series(paths))
    assert all(data.get(column.SIZE) == Series(range(len(paths))))
    assert all(data.get(column.TYPE) == Series(['.a', '.b', '.c']))


def test_type_size_data():
    test_dir = dirname(__file__)
    data = _csft.csft2data(test_dir)
    assert isinstance(data, DataFrame)
    assert data['type'].str.contains('py').sum()
