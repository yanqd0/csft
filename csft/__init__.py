# -*- coding:utf-8 -*-

"""
Count Sizes of File Types
"""

__author__ = 'Yan QiDong'
__version__ = '0.3.0'
__email__ = 'yanqd0@outlook.com'
__url__ = 'https://github.com/yanqd0/csft'
__copyright__ = 'Copyright (C) 2017 ' + __author__
__license__ = 'MIT License'

try:
    from pkg_resources import DistributionNotFound, get_distribution
except ImportError:
    __version__ = 'x.x.x.dev'
else:
    try:
        __version__ = get_distribution(__name__).version
    except DistributionNotFound:
        __version__ = 'x.x.x.dev'


def _err_func(error):
    def _func(*args, **kwargs):
        print(args, kwargs)
        raise error

    return _func


try:
    from ._csft import csft2data
except ImportError as err:
    print(err)
    csft2data = _err_func(err)
