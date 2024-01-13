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

    try:
        filename = archive_path.split("/")[-1]
        no_extension = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_extension))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, path,  no_extension))
        run("rm /tmp/{}".format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))
        run('rm -rf {}{}/web_static'.format(path, no_extension))
        run("rm -rf /data/web_static/current")
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        print("New version deployed!")
        return True
    except Exception:
        return False
