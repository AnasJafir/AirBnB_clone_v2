#!/usr/bin/python3
"""
Fabric script that creates and distributes
an archive to your web servers
"""


from fabric.api import *
from datetime import datetime
from os.path import exists, isdir


env.hosts = ['54.157.175.161', '52.91.136.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """generates archive file"""
    try:
        date_ = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


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


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
