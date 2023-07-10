#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from fabric.api import local
import time


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    time_now = time.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(time_now)
    local('mkdir -p versions')
    local('tar -cvzf {} web_static'.format(archive_path))
    return archive_path


def print_output():
    archive_path = do_pack()
    print(
        'web_static packed: {} -> {}Bytes'.format(
            archive_path,
            local('ls -l {} | cut -d " " -f 5'.format(archive_path))))


if __name__ == '__main__':
    print_output()
