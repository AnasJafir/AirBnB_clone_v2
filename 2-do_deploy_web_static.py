#!/usr/bin/python3
"""Module of Deploy"""
from fabric.api import local, put, run, env
import os

env.hosts = ['54.146.9.154', '54.152.182.247']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    # check if the file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # define the archive filename and directory path
        archive_filename = os.path.basename(archive_path)
        archive_dir = "/data/web_static/releases/" + archive_filename[:-4]

        # run commands on the server
        # create directory
        run("sudo mkdir -p {}".format(archive_dir))
        # uncompress the archive
        run("sudo tar -xzf /tmp/{} -C {}".format(
            archive_filename, archive_dir
            ))
        # delete the archive
        run("sudo rm /tmp/{}".format(archive_filename))
        # delete the symbolic link
        run("sudo rm -rf /data/web_static/current")
        # create a new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(archive_dir))

        return True
    except Exception:
        return False
