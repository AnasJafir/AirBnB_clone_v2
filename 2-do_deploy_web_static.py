#!/usr/bin/python3
"""
Fabric script that distributes
an archive to your web servers
"""


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['54.157.175.161', '52.91.136.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    # Check if the archive file exists in the archive_path
    if exists(archive_path) is False:
        return False
    # Store the file web_static_20240112161003.tgz in filename
    filename = archive_path.split('/')[-1]

    no_extension = '/data/web_static/releases/' + "{}".format(
            filename.split('.')[0]
            )
    tmp = "/tmp/" + filename

    try:
        # ^ Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Extract the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("mkdir -p {}/".format(no_extension))
        run("tar -xzf {} -C {}/".format(tmp, no_extension))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_extension, no_extension))
        # Delete the archive from the web server
        run("rm -rf {}/web_static".format(no_extension))
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {}/ /data/web_static/current".format(no_extension))
        return True
    except Exception:
        return False
