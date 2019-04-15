import os

from compas.datastructures import Mesh
from compas.datastructures import mesh_flatness
from compas.utilities import i_to_rgb
from compas.rpc import Proxy

from compas_rhino.artists import MeshArtist


planarization = Proxy('compas_meshx.planarization')


# define the location of the current file
HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'tubemesh.json')

# make a mesh from a JSON file
mesh1 = Mesh.from_json(FILE)

# extract the vertices and faces of the mesh
vertices, faces = mesh1.to_vertices_and_faces()

# compute the vertices of the planarized mesh
planar = planarization.planarize(vertices, faces)

# make a new mesh from the new vertex coordinates
mesh2 = Mesh.from_vertices_and_faces(planar, faces)

# compute the deviation from "flat" per face of both meshes
dev1 = mesh_flatness(mesh1, maxdev=0.02)
dev2 = mesh_flatness(mesh2, maxdev=0.02)

# compute the color of each face based on its flatness
facecolors = {fkey: i_to_rgb(dev2[fkey]) for fkey in mesh2.faces()}

# visualize the result
artist = MeshArtist(mesh2)
artist.draw_faces(color=facecolors)

