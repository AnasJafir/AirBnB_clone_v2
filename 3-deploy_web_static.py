#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers

execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os
env.hosts = ['54.160.77.90', '10.25.190.21']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """generates a tgz archive"""
    # create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # create a timestamped filename
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date_time)

    # use the local fabric command to create an archive file
    result = local("tar -cvzf {} web_static".format(filename))

    # return the archive path if the file was created successfully
    if result is not None:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
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


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
