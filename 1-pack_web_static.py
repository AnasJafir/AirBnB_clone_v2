#!/usr/bin/python3
"""Module of Generating an archive file with Fabric"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
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
