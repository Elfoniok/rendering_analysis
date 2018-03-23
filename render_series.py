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
width = params['width']
height = params['height']

for samples in range(params['start'],params['end'],params['step']):
    for scene in bpy.data.scenes:
        scene.render.resolution_x = width
        scene.render.resolution_y = height
        scene.cycles.samples = samples
        scene.cycles.seed = seed
        scene.render.filepath = os.path.join(output_path,
                                             "image_{0:05d}_{1}_{2}_{3}.png".format(n,
                                                                                    width,
                                                                                    height,
                                                                                    samples))
    n += 1
    if increment:
        seed += 1
    bpy.ops.render.render(write_still=True)
