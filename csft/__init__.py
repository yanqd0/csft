# -*- coding:utf-8 -*-

"""
Count Sizes of File Types
"""

from csft._csft import csft2data

__author__ = 'Yan QiDong'
__email__ = 'yanqd0@outlook.com'
__url__ = 'https://github.com/yanqd0/csft'
__copyright__ = 'Copyright (C) 2017 ' + __author__
__license__ = 'MIT License'


def _get_version(default='x.x.x.dev'):
    try:
        from pkg_resources import DistributionNotFound, get_distribution
    except ImportError:
        return default
    else:
        try:
            return get_distribution(__name__).version
        except DistributionNotFound:
            return default


__version__ = _get_version()
