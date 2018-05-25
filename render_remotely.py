import sys
import pickle
from upload_scenes import create_connection, upload_scene, prepare_remote_env, render_series

address = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]

scene_dir = sys.argv[5]

host = { 'address': address, 'port': port}

client = create_connection(host, user, password)
remote_files = upload_scene(scene_dir, host, "render_series", client)
# with open('filename.pickle', 'wb') as handle:
#     pickle.dump(remote_files, handle, protocol=pickle.HIGHEST_PROTOCOL)
# with open('filename.pickle', 'rb') as handle:
#     remote_files = pickle.load(handle)

for paths in remote_files[host['address']]:
    remote_path = paths[0]
    prepare_remote_env(remote_path, client)
    render_series(client, host, paths[1], seed=0, inc_seed=0, start=1, end=2, step=1)




