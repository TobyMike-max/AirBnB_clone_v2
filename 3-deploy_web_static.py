#!/usr/bin/python3
"""Fabfile to generate a .tgz archive from the contents of web_static.
    & Fabfile to distribute an archive to a web server."""
from fabric.api import local
from 2-do_deploy_web_static import do_pack
from 3-deploy_web_static import do_deploy

env.hosts = ["3.235.20.78", "44.201.70.161"]
env.user = ["ubuntu"]


def deploy():
    """Create and distributes an archive to a web server.
    """
    path = local(do_pack())
    if path.failed is True:
        return False
    return local(do_deploy(path))
