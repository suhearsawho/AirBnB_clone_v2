#!/usr/bin/python3
"""Deploy function"""
from fabric.api import *

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """Fabric script that creates and distributes an archive to web servers"""
    archive = do_pack()
    if archive == None:
        return False

    env.hosts = ['35.185.66.253', '35.229.43.253']
    return do_deploy(archive)
