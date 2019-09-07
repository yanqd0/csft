#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" Setup script for csft """
from distutils.version import LooseVersion
from runpy import run_path
from sys import version

from setuptools import find_packages, setup

REQUIRES = [
    'pandas >= 0.20.3',
    'humanfriendly >= 4.6',
]
SYS_VERSION = LooseVersion(version)
if SYS_VERSION < LooseVersion('3.4'):
    REQUIRES.append('pathlib >= 1.0.1')
if SYS_VERSION < LooseVersion('3.5'):
    REQUIRES[0] = 'pandas >= 0.20.3, < 0.22'
    REQUIRES.append('scandir >= 1.5')

INFO = run_path('src/csft/_meta.py')

setup(
    # metadata
    name='csft',
    description='Count Sizes of File Types',
    url=INFO['__url__'],
    author=INFO['__author__'],
    author_email=INFO['__email__'],
    license=INFO['__license__'],
    use_scm_version=True,
    # package
    zip_safe=False,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ('csft = csft.__main__:main', ),
    },
    # requires
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
        'pytest-isort',
        'pytest-yapf3',
        'mock',
    ],
    # PyPI
    keywords=['CLI'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
