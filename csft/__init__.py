# -*- coding:utf-8 -*-

"""
Count Sizes of File Types
"""

from csft._csft import csft2data

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
    finally:
        del DistributionNotFound, get_distribution
