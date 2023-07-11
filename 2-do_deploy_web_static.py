#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of
AirBnB_clone_v2 web_static folder"""

from datetime import datetime
import os
from fabric.api import env, put, run, sudo, local, settings


# Define your server IP and credentials
env.hosts = ["54.145.240.186", "54.175.134.147"]
env.user = "ubuntu"
env.key_filename = "/root/.ssh/id_rsa"

def do_pack():
    '''Generates a .tgz archive from the contents of the web_static folder
    of AirBnB_clone_v2

    Returns:
        str: Path to the archive created'''

    if not os.path.isdir("versions"):
        os.makedirs("versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)

    print("Packing web_static to {}".format(file_name))
    with settings(warn_only=True):
        result = local("tar -cvzf {} web_static".format(file_name))
        if result.failed:
            return None
    file_size = os.stat(file_name).st_size
    print("web_static packed: {} -> {}Bytes".format(file_name, file_size))

    return file_name



def do_deploy(archive_path):
    """Distributes an archive to the web servers and deploys it"""
    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    remote_path = "/tmp/{}".format(archive_name)
    release_path = "/data/web_static/releases/{}".format(
        archive_name.replace(".tgz", "").replace("web_static_", "")
    )

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, remote_path)

    # Uncompress the archive to the release_path on the web server
    run("mkdir -p {}".format(release_path))
    run("tar -xzf {} -C {}".format(remote_path, release_path))

    # Delete the archive from the web server
    run("rm {}".format(remote_path))

    # Move the contents of the web_static folder to the release_path
    run("mv {}/web_static/* {}".format(release_path, release_path))

    # Remove the empty web_static folder
    run("rm -rf {}/web_static".format(release_path))

    # Delete the symbolic link /data/web_static/current from the web server
    run("rm -rf /data/web_static/current")

    # Create a new symbolic link to the new version of your code
    run("ln -s {} /data/web_static/current".format(release_path))

    print("New version deployed!")
    return True
