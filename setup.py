#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" Setup script for csft """

from setuptools import find_packages, setup

import csft

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
    install_requires=(
        'argparse>=1.2.1',
        'pandas>=0.20.1',
        'numpy>=1.12.1',
    ),
)
