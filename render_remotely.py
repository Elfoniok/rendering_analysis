import sys
from upload_scenes import create_connection, upload_scene, prepare_remote_env, render_series

address = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]

scene_dir = sys.argv[5]

host = { 'address': address, 'port': port}

client = create_connection(host, user, password)
remote_files = upload_scene(scene_dir, host, scene_dir, client)
remote_path = remote_files[host['address']][0]
prepare_remote_env(remote_path, client)
render_series(client, host, remote_files, seed=10, inc_seed=0, start=1, end=100, step=25)




