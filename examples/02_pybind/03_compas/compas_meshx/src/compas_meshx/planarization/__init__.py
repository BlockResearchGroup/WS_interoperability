"""
********************************************************************************
compas_meshx.planarization
********************************************************************************

.. currentmodule:: compas_meshx.planarization

Classes
=======

.. autosummary::
    :toctree: generated/
    :nosignatures:

Functions
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    planarize

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from . import planarization


def planarize(vertices, faces):
    from numpy import array, float64, int32
    V1 = array(vertices, dtype=float64)
    F1 = array(faces, dtype=int32)
    V2 = planarization.planarize(V1, F1)
    return V2.tolist()


__all__ = [name for name in dir() if not name.startswith('_')]
