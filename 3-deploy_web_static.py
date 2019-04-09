#!/usr/bin/python3
"""Deploy function"""
from fabric.api import *
import datetime
import os

env.hosts = ['35.185.66.253', '35.229.43.253']


@runs_once
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
        run('tar -xzf /tmp/{} -C {}'.format(archive_path[9:], path))
        run('rm /tmp/{}'.format(archive_path[9:]))
        run('mv {}web_static/* {}'.format(path, path))
        run('rm -rf {}web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(path))
    except:
        return False
    else:
        print('New version deployed!')
        return True


def deploy():
    """Fabric script that creates and distributes an archive to web servers"""
    archive = do_pack()
    if archive is None:
        return False

    return do_deploy(archive)
