#!/usr/bin/python3
"""Contains do_pack function"""
import datetime
from fabric.api import *


def do_pack():
    """This function generates a .tgz archive from contents of
    web_static folder of AirBnb Clone repo
    """
    now = datetime.datetime.now()
    path = 'versions/web_static_' +\
           '{}{}{}{}{}{}'.format(now.year, now.month,
                                 now.day, now.hour,
                                 now.minute, now.second) + '.tgz'

    local('mkdir -p versions')
    success = local('tar -cvzf {:s} web_static'.format(path), capture=True)
    if success.return_code == 0:
        return path
