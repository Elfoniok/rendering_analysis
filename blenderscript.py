import bpy
import sys

width = 800
height = 600

n = 0
seed = 0

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

for scene in bpy.data.scenes:
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.cycles.seed = seed
    scene.render.filepath = argv[0]
    
bpy.ops.render.render(write_still=True)
