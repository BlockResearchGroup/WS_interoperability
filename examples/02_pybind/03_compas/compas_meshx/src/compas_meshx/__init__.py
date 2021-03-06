"""
********************************************************************************
compas_meshx
********************************************************************************

.. currentmodule:: compas_meshx


.. toctree::
    :maxdepth: 1

    compas_meshx.isolines
    compas_meshx.planarization

"""

from __future__ import print_function

import os
import sys


__author__ = ['tom van mele <vanmelet@ethz.ch>']
__copyright__ = 'Block Research Group - ETH Zurich'
__license__ = 'MIT License'
__email__ = 'vanmelet@ethz.ch'
__version__ = '0.1.0'


HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, '../../'))
DATA = os.path.abspath(os.path.join(HOME, 'data'))
DOCS = os.path.abspath(os.path.join(HOME, 'docs'))
TEMP = os.path.abspath(os.path.join(HOME, 'temp'))


__all__ = ['HOME', 'DATA', 'DOCS', 'TEMP']
