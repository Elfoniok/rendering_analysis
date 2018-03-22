import os
import subprocess
import sys
from multiprocessing import cpu_count

def find_scenes():
    output_dir = os.getcwd()

    scene_paths = []

    for root, dirs, files in os.walk(output_dir):
        for name in files:
            if name.endswith('.blend'):
                scene_paths.append(os.path.join(root, name))
    return scene_paths
		
BLENDER_COMMAND = "blender"

def exec_cmd(cmd):
    pc = subprocess.Popen(cmd)
    return pc.wait()


def format_blender_render_cmd(outfilebasename, scene_file, script_file):
    cmd = [
        "{}".format(BLENDER_COMMAND),
        "-b", "{}".format(scene_file),
        "-y",  # enable scripting by default
        "-noaudio",
        "-t", "{}".format(cpu_count()),
        "-P", "{}".format(script_file),
        "--", "{}".format(outfilebasename)
    ]
    return cmd


def run_blender():

    scenes = find_scenes()

    for scene in scenes:
        scene_file = os.path.normpath(scene)
        if not os.path.exists(scene_file):
            print("Scene file '{}' does not exist".format(scene_file),
                file=sys.stderr)
            sys.exit(1)

        out_file_path = os.path.dirname(scene)
        out_file_name = os.path.join(out_file_path, "image_default")
        cmd = format_blender_render_cmd(out_file_name, scene,
                                        "blenderscript.py")
        print(cmd, file=sys.stderr)
        exit_code = exec_cmd(cmd)
        if exit_code is not 0:
            sys.exit(exit_code)


run_blender()
