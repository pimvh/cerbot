import testinfra


def test_certbot_config(host):
    assert host.file("/etc/letsencrypt/cli.ini").contains("key-type = ecdsa")
    assert host.file("/etc/letsencrypt/cli.ini").contains("elliptic-curve = secp384r1")

    assert host.file("/etc/letsencrypt/cli.ini").contains("rsa-key-size = 4096")
