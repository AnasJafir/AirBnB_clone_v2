#!/usr/bin/python3
"""
Fabric script that generates a
.tgz archive from the contents of the web_static folder
"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Method that generates a .tgz archive
    from the contents of the web_static folder
    """

    # Create the versions directory if it's doesn't exist
    local("mkdir -p versions")

    # Precize the date
    date_ = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the archive
    archive_file = "versions/web_static_{}.tgz".format(date_)
    result = local("tar -cvzf {} web_static".format(archive_file))

    # Return the archive path if the archive is correctly generated
    # Otherwise Return None
    if result.failed:
        return None
    else:
        return archive_file
