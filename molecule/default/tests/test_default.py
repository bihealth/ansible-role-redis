import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_conf_file(host):
    if host.system_info.distribution in ('debian', 'ubuntu'):
        f = host.file('/etc/redis/redis.conf')
        group = 'redis'
    else:
        f = host.file('/etc/redis.conf')
        group = 'root'

    assert f.exists
    assert f.user == 'redis'
    assert f.group == group


def test_internal_socket(host):
    assert host.socket("tcp://127.0.0.1:6379").is_listening


def test_external_socket(host):
    assert not host.socket("tcp://0.0.0.0:6379").is_listening
