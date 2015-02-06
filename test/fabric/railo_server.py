# coding=utf8
from fabric.api import env, task
from envassert import detect, file, port, process, service

from hot.utils.test import get_artifacts, http_check


@task
def check():
    env.platform_family = detect.detect()

    site = "http://localhost/"
    string = "Apache2 Ubuntu Default Page"

    assert file.exists("/opt/railo/install.log"), "Railo install log missing."
    assert port.is_listening(80), "Port 80 is not listening."
    assert port.is_listening(8888), "Port 8888 is not listening."
    assert process.is_up("java"), "The java process is not running."
    assert service.is_enabled("apache2"), "The apache2 service is not enabled."
    assert service.is_enabled("railo_ctl"), "The Railo service is not enabled."
    assert http_check(site, string), "Apache is not responding."


@task
def artifacts():
    env.platform_family = detect.detect()

    # Logs to pull
    logs = ['/root/cfn-userdata.log',
            '/root/heat-script.log']

    get_artifacts(logs)
