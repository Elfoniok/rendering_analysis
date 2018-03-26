import paramiko
import tarfile
import os
import scp


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


def create_sshclient(server, port, user, password=None):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def create_connection(host, user, password):
    client = create_sshclient(host['address'], host['port'], user, password)
    return client


def prepare_remote_env(remote_path, client):
    file_name = os.path.basename(remote_path)
    index_of_dot = file_name.index('.')
    name = file_name[:index_of_dot]

    client.exec_command(str("mv {} {}/.", remote_path, name))
    #tar = tarfile.open(remote_file, "r:gz")


def upload_scene(scenes_dir, host, remote_path, client):
    remote_files = dict()
    for scene in find_scenes(scenes_dir):

        name = os.path.dirname(scene)
        client.exec_command(str("mkdir {}", name))
        arc_name = name + ".tgz"

        make_tarfile(arc_name, scene)

        scp_client = scp.SCPClient(client.get_transport())
        # or
        #client = scp.Client(host=host, user=user, keyfile=keyfile)
        # or
        #client = scp.Client(host=host, user=user)
        #client.use_system_keys()

        remote_file = os.path.join(remote_path, arc_name)

        scp_client.put(arc_name, remote_file)

        remote_files[host['address']] = remote_file
    return remote_files
