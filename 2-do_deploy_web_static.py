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
    if os.path.exists(archive_path) is False:
        return False

    try:
        # define the archive filename and directory path
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        # run commands on the server
        # create directory
        run('mkdir -p {}{}/'.format(path, no_ext))
        # uncompress the archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        # delete the archive
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        # delete the symbolic link
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        # create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
