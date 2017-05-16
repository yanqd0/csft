#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" Setup script for csft """

import sys

from setuptools import find_packages, setup

import csft

ver = sys.version

requires = [
    'pandas >= 0.20.1',
]

if ver > '3.0' and ver < '3.2':
    requires.append('argparse >= 1.4.0')

if ver < '3.4':
    requires.append('pathlib >= 1.0.1')

if ver < '3.5':
    requires.append('scandir >= 1.5')

setup(
    name=csft.__name__,
    description=csft.__doc__,
    version=csft.__version__,
    author=csft.__author__,
    license=csft.__license__,
    author_email=csft.__email__,
    url=csft.__url__,
    packages=find_packages(),
    entry_points={
        'console_scripts': (
            'csft = csft.__main__:main',
        ),
    },
    python_requires='>=2.7',
    install_requires=requires,
)
