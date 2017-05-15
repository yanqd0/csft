#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
The entry point of csft.
"""

import argparse as ap
from os.path import isdir

from .csft import print_result


def main():
    parser = ap.ArgumentParser(add_help='add help')
    parser.add_argument('location', help='the directory to be analyzed')
    args = parser.parse_args()
    if not isdir(args.location):
        raise TypeError('%s is not a directory!', args.location)
    return print_result(args.location)


if __name__ == '__main__':
    raise SystemExit(main())
