#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
The entry point of csft.
"""

import argparse as ap
from os.path import isdir

from . import __name__ as _name
from . import __version__ as _version
from .csft import csft2data


def _positive_int(num):
    number = int(num)
    if number <= 0:
        raise ValueError('%s is not positive!', number)
    return number


def _parse_args(argv):
    parser = ap.ArgumentParser(prog=_name)
    parser.add_argument('-V', '--version', action='version', version=_version)
    parser.add_argument('path', help='the directory to be analyzed')
    parser.add_argument('--top', type=_positive_int, metavar='N',
                        help='only display top N results')

    args = parser.parse_args(args=argv)
    if not isdir(args.path):
        raise TypeError('%s is not a directory!', args.path)
    return args


def main(argv=None):
    """Execute the application from CLI."""
    args = _parse_args(argv)
    data = csft2data(args.path)

    if args.top:
        data = data.head(args.top)

    print(data)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
