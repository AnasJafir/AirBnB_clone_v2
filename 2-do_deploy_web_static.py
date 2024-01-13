#!/usr/bin/python3
"""
Fabric script that distributes
an archive to your web servers
"""


from fabric.api import *
from os.path import exists


env.hosts = ['54.157.175.161', '52.91.136.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    # Check if the archive file exists in the archive_path
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract archive to the folder
        # /data/web_static/releases/web_static_20240112161003 on the web server
        file_name = archive_path.split("/")[-1]
        no_extension, extension = file_name.split(".")
        run("mkdir -p /data/web_static/releases/{}/".format(no_extension))
        run("tar -xzf /tmp/{} "
            "-C /data/web_static/releases/{}/".format(file_name, no_extension))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        # /data/web_static/current on the web server
        # linked to the new version of your code
        # (/data/web_static/releases/web_static_20240112161003)
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(no_extension))

        return True
    except Exception:
        return False
