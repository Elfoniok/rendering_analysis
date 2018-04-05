import paramiko
import tarfile
import os
import scp

#TODO
# Add absolute path support
# Add pubkey authorization
# Implement lookup and collecting

def create_sshclient(server, port, user, password=None):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def create_connection(host, user, password):
    client = create_sshclient(host['address'], host['port'], user, password)
    return client

def upload_scene(scenes_dir, host, remote_path, client):
    """
    :param remote_path
    """
    
    remote_files = dict()
    for scene in find_scenes(scenes_dir):

        name = os.path.dirname(scene)

        remote_scene_dir = os.path.join(remote_path, name)

        client.exec_command(str("mkdir -p {}".format(remote_scene_dir)))
        arc_name = name + ".tgz"

        make_tarfile(arc_name, scene)

        scp_client = scp.SCPClient(client.get_transport())
        # or
        #client = scp.Client(host=host, user=user, keyfile=keyfile)
        # or
        #client = scp.Client(host=host, user=user)
        #client.use_system_keys()

        remote_file = os.path.join(remote_scene_dir, arc_name)

        scp_client.put(arc_name, remote_file)

        remote_files[host['address']] = (remote_file, os.path.join(
            remote_scene_dir, os.path.basename(scene)))
    return remote_files

def prepare_remote_env(remote_path, client):
    dir_name = os.path.dirname(remote_path)
    client.exec_command(str("tar -xvzf {} -C {}".format(remote_path,
        dir_name)))
    scp_client = scp.SCPClient(client.get_transport())
    scp_client.put('render_series.py', dir_name)

def render_series(client, host, remote_path,
     seed=0, inc_seed=1, output_path="output", width=800, height=600, start=0, end=10000, step=100):
    dir_name = os.path.dirname(remote_path[host['address']][0])
    blender_script_params = "\"{\\\"seed\\\": %r," \
    "\\\"increment_seed\\\": %r," \
    "\\\"output_path\\\":\\\"%s\\\"," \
    "\\\"width\\\": %r," \
    "\\\"height\\\":%r," \
    "\\\"start\\\": %r," \
    "\\\"end\\\": %r," \
    "\\\"step\\\": %r}\"" % (seed, inc_seed, os.path.join(dir_name, output_path), width, height, start, end, step)
    remote_script_path = os.path.join(dir_name, "render_series.py")
    log_path = os.path.join(dir_name, "log")
    render_command = str("nohup blender -b "+
        str(remote_path[host['address']][1]) +
        " -P " + remote_script_path + " -- " +
        blender_script_params +
        " > " + log_path + " &")
    print(render_command)
    client.exec_command(render_command)

def lookup_progress():
    pass

def collect_results():
    pass

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def find_scenes(scenes_dir):
        scene_paths = []
        for root, dirs, files in os.walk(scenes_dir):
            for name in files:
                if name.endswith('.blend'):
                    scene_paths.append(os.path.join(root, name))
        return scene_paths
