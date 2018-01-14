#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" Setup script for csft """
from sys import version

from setuptools import find_packages, setup

import csft

REQUIRES = [
    'pandas >= 0.20.3',
    'humanfriendly >= 4.6',
]

if version < '3.4':
    REQUIRES.append('pathlib >= 1.0.1')

if version < '3.5':
    REQUIRES[0] = 'pandas >= 0.20.3, < 0.22',
    REQUIRES.append('scandir >= 1.5')

setup(
    name=csft.__name__,
    use_scm_version=True,
    description='Count Sizes of File Types',
    url=csft.__url__,
    author=csft.__author__,
    author_email=csft.__email__,
    license=csft.__license__,

    packages=find_packages(),
    entry_points={
        'console_scripts': (
            'csft = csft.__main__:main',
        ),
    },

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=REQUIRES,
    setup_requires=[
        'pytest-runner',
        'setuptools_scm',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
        'pytest-flakes',
        'pytest-mock',
        'mock',
    ],

    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
