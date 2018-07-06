import sys
import pickle
from upload_scenes import create_connection, upload_scene, prepare_remote_env, render_series
from pathlib import Path

import scenes_params


## ======================= ##
##
def run():

    address = sys.argv[1]
    port = sys.argv[2]
    user = sys.argv[3]
    password = sys.argv[4]

    scene_dir = sys.argv[5]

    host = { 'address': address, 'port': port}

    client = create_connection(host, user, password)
    remote_files = upload_scene(scene_dir, host, "render_series5/", client)
    
    # with open('filename.pickle', 'wb') as handle:
    #     pickle.dump(remote_files, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('filename.pickle', 'rb') as handle:
    #     remote_files = pickle.load(handle)

    for paths in remote_files[host['address']]:
    
        remote_path = paths[0]
        
        scene_name = scenes_params.get_scene_name( remote_path )
        params = scenes_params.get_scene_parameters( scene_name )
        
        print( "Rendering scene: [" + scene_name + "] with parameters: " )
        scenes_params.print_scene_parameters( params )
        
        prepare_remote_env(remote_path, client)
        
        render_series(client, host, paths[1], seed=params.seed, inc_seed=params.inc_seed,
         start=params.start, end=params.end, step=params.step, filename=Path(paths[1]).resolve().stem,
         width=params.width, height=params.height, pref_device="OPENCL")



if __name__ == "__main__":
    run()

