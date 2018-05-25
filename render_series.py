import bpy
import sys
import json
import os

n = 0

argv = sys.argv
#get all args after "--"
argv = argv[argv.index("--") + 1:]

params = json.loads(argv[0])
seed = params['seed']
increment = params['increment_seed']
output_path = params['output_path']

#Use default if not defined
width = params['width']
height = params['height']

def render_once(width, height, samples, seed):
    if width != 0:
        bpy.context.scene.render.resolution_x = width
    if height != 0:
        bpy.context.scene.render.resolution_y = height
    bpy.context.scene.cycles.samples = samples
    bpy.context.scene.cycles.seed = seed
    bpy.context.scene.render.filepath = os.path.join(output_path,
                                             "image_{0}.png".format(samples))
    bpy.ops.render.render(write_still=True)

for samples in range(params['start'],params['end'],params['step']):
    render_once(width, height, samples, seed)
    if increment:
        seed += 1

#render maximum sample image despite current stepping
render_once(width, height, params['end'], seed)
