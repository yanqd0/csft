# -*- coding:utf-8 -*-

"""
The implementations of csft.
"""

import sys
from collections import OrderedDict
from os.path import split, splitext

from pandas import DataFrame, Series
from pathlib import Path

if sys.version <= '3.5':
    from scandir import walk
else:
    from os import walk


class Column(object):
    PATH = 'path'
    SIZE = 'size'
    TYPE = 'type'


def _find_path_list(path):
    paths = []
    for parent, _, files in walk(path):
        parent_path = Path(parent)
        for name in files:
            file_path = parent_path.joinpath(name)
            if not file_path.is_symlink():
                paths.append(file_path)
    return paths


def _file_type(file_path):
    _, file_name = split(file_path)
    _, file_type = splitext(file_name)
    return file_type


def _generate_raw_data_from(paths):
    str_paths = Series([str(path) for path in paths])
    sizes = Series([path.stat().st_size for path in paths])
    data = DataFrame({
        Column.PATH: str_paths,
        Column.SIZE: sizes,
    })
    data[Column.TYPE] = data[Column.PATH].map(_file_type)
    return data


def _add_type_to(data):
    types = set()
    for file_type in data['type']:
        types.add(file_type)
    return data, types


def _type_size_sum(data, types):
    sizes = []
    for file_type in types:
        type_data = data[data[Column.TYPE] == file_type]
        sizes.append(type_data[Column.SIZE].sum())
    return Series(sizes)


def _generate_type_data_from(data):
    types = set([file_type for file_type in data[Column.TYPE]])
    types = Series(tuple(types))
    sizes = _type_size_sum(data, types)

    type_size = OrderedDict()
    type_size[Column.TYPE] = types
    type_size[Column.SIZE] = sizes
    return DataFrame(type_size)


def _sort_by_size(data):
    data = data.sort_values(Column.SIZE, ascending=False)
    return data.reset_index()


def print_result(path):
    paths = _find_path_list(path)
    raw_data = _generate_raw_data_from(paths)
    type_data = _generate_type_data_from(raw_data)
    sorted_data = _sort_by_size(type_data)
    print(sorted_data)
