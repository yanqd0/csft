csft - Count Sizes of File Types
================================

.. image:: https://travis-ci.org/yanqd0/csft.svg?branch=master
    :target: https://travis-ci.org/yanqd0/csft
.. image:: https://codecov.io/gh/yanqd0/csft/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/yanqd0/csft
.. image:: https://img.shields.io/github/license/yanqd0/csft.svg
    :target: https://github.com/yanqd0/csft/blob/master/LICENSE

A CLI to count sizes of file types in a directory, implemented by Python.

Install
--------

.. image:: https://img.shields.io/pypi/v/csft.svg
   :target: https://pypi.python.org/pypi/csft
.. image:: https://img.shields.io/pypi/format/csft.svg
   :target: https://pypi.python.org/pypi/csft
.. image:: https://img.shields.io/pypi/pyversions/csft.svg
   :target: https://pypi.python.org/pypi/csft

Install from the official PYPI::

    pip install csft

Install from the latest source::

    pip install git+https://github.com/yanqd0/csft.git

.. image:: https://img.shields.io/github/release/yanqd0/csft.svg
   :target: https://github.com/yanqd0/csft/releases
.. image:: https://img.shields.io/github/issues/yanqd0/csft.svg
   :target: https://github.com/yanqd0/csft/issues

Usage
-----

The simplest usage::

    csft PATH/TO/YOUR/PROJECT

More Usage::

    csft -h

Result
------

Something like this::

           type   size
    0            32859
    1   .sample  15321
    2      .xml  12349
    3      .pyc   7100
    4       .py   4221
    5      .yml   1085
    6      .rst    638
    7      .iml    455
    8        .2     41
    9        .1     41
    10       .0     41
