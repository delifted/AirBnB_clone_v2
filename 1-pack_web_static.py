#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of
AirBnB_clone_v2 web_static folder
"""
'''from datetime import datetime
from fabric.api import local, settings
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    of AirBnB_clone_v2

    Returns:
        str: Path to the archive created
    """
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
'''

from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
