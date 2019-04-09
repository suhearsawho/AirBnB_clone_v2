#!/usr/bin/python3
"""Introduces the do_deploy function"""
import os
from fabric.api import *

env.hosts = ['35.185.66.253', '35.229.43.253']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if os.path.isfile(str(archive_path)) is 0:
        return False

    path = '/data/web_static/releases/{}/'.format(archive_path[9:-4])
    try:
        # Upload archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        # Uncompress the archive to the folder
        run('mkdir -p {}'.format(path))
        with cd('/tmp/'):
            run('tar -xzf /tmp/{} -C {}'.
                format(archive_path[9:], path))
            run('rm /tmp/{}'.format(archive_path[9:]))
        run('mv {}web_static/* {}'.format(path, path))
        run('rm -rf {}web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
    except:
        return False
    else:
        return True
