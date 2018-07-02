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
filename = params['filename']

#possible
#CUDA
#OPENCL
#CPU ?
#NONE
pref_device = params['pref_device']

for device in bpy.context.user_preferences.addons['cycles'].preferences.devices:
    if device.type == pref_device:
        device.use=True
        bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = device.type

if pref_device == "CUDA" or pref_device == "OPENCL":
    bpy.context.scene.cycles.device = "GPU"
else:
    bpy.context.scene.cycles.device = "CPU"

def render_once(width, height, samples, seed):
    if width != 0:
        bpy.context.scene.render.resolution_x = width
    if height != 0:
        bpy.context.scene.render.resolution_y = height
    bpy.context.scene.cycles.samples = samples
    bpy.context.scene.cycles.seed = seed
    bpy.context.scene.render.resolution_percentage = 100
    bpy.context.scene.render.filepath = os.path.join(output_path,
                                             "{0}_[samples={1}].png".format(filename, samples))
    bpy.ops.render.render(write_still=True)

for samples in range(params['start'],params['end'],params['step']):
    render_once(width, height, samples, seed)
    if increment:
        seed += 1

#render maximum sample image despite current stepping
render_once(width, height, params['end'], seed)
