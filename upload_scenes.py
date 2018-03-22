import paramiko
import tarfile
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

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def upload_scenes(scenes_dir, hosts_list, user, remote_path):

    for scene in zip(find_scenes(scenes_dir), hosts_list):

        arc_name = os.path.dirname(scene) + ".tgz"

        make_tarfile(arc_name , scene)

        client = createSSHClient(node['address'], node['port'], user)
        scpClient = scp.SCPClient(client.get_transport())
        # or
        #client = scp.Client(host=host, user=user, keyfile=keyfile)
        # or
        #client = scp.Client(host=host, user=user)
        #client.use_system_keys()

       remote_file = os.path.join(remote_path, arc_name)

       scpClient.put(arc_name, remote_file)

       remote_files[node['address']] = remote_file
       return remote_files
