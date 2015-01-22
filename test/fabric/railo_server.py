# coding=utf8

import re

from fabric.api import env, hide, run, task
from envassert import detect, file, package, port, process, service


def apache_is_responding():
    with hide('running', 'stdout'):
        site = "http://localhost/"
        homepage = run("wget --quiet --output-document - --no-check-certificate %s" % site)
        if re.search('Apache2 Ubuntu Default Page', homepage):
            return True
        else:
            return False


@task
def check():
    env.platform_family = detect.detect()

    assert file.exists("/opt/railo/install.log"), "Railo install log missing."
    assert port.is_listening(80), "Port 80 is not listening."
    assert port.is_listening(8888), "Port 8888 is not listening."
    assert process.is_up("java"), "The java process is not running."
    assert service.is_enabled("apache2"), "The apache2 service is not enabled."
    assert service.is_enabled("railo_ctl"), "The Railo service is not enabled."
    assert apache_is_responding(), "Apache is not responding."
