import os
import sys
import numpy

from itertools import groupby

import compas

from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles
from compas_plotters import MeshPlotter
from compas.utilities import i_to_rgb


# define the location of the current file
HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'tubemesh.json')

# insert the path to the compiled libraries in PYTHONPATH
sys.path.insert(0, os.path.join(HERE, '../modules'))

# import one of the compiled libraries
import isolines

# make a quad mesh from a JSON file
# and convert to a triangle mesh
mesh = Mesh.from_json(FILE)
mesh_quads_to_triangles(mesh)

# convert the mesh to vertex coordinates
# and face vertex lists
vertices, faces = mesh.to_vertices_and_faces()

# convert lists to arrays
V = numpy.array(vertices, dtype=numpy.float64)
F = numpy.array(faces, dtype=numpy.int32)

# get the Z cooridnates of the vertices
# and define the number of contours
Z = V[:, 2]
N = 100

# compute the contour lines
result = isolines.contours(V, F, Z, N)

# group the contour line segments per Z
edges = groupby(result.edges, key=lambda e: result.vertices[e[0]][2])

# compute min and max Z for colouring
zmin = min(Z)
zmax = max(Z)

# create drawing data
# use a different colour per group of edges
# assign the colur based on the Z of the group
lines = []
for z, group in edges:
    color = i_to_rgb((z - zmin) / (zmax - zmin))
    for i, j in group:
        lines.append({
            'start' : result.vertices[i],
            'end'   : result.vertices[j],
            'color' : color
        })

# visualize the result
plotter = MeshPlotter(mesh, figsize=(10, 7))
plotter.draw_faces()
plotter.draw_lines(lines)
plotter.show()
