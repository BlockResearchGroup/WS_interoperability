import os
import bpy

from compas.datastructures import Mesh
from compas.datastructures import mesh_flatness
from compas.utilities import i_to_rgb

from compas_blender.artists import MeshArtist

from compas_meshx import planarization


# define the location of the current file
HERE = os.path.dirname(bpy.context.space_data.text.filepath)
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
facecolors = {}
for fkey in mesh2.faces():
    r, g, b = i_to_rgb(dev2[fkey])
    facecolors[fkey] = [r / 255.0, g / 255.0, b / 255.0]

# clean the scene
for o in bpy.data.objects:
    o.select_set(True)
bpy.ops.object.delete()

# visualize the result
artist = MeshArtist(mesh2)
artist.draw_faces(colors=facecolors)

