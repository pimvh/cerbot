import testinfra


def test_os_release(host):
    """test host release for good measure"""

    assert host.file("/etc/os-release").contains("Ubuntu")


def test_certbot_config(host):
    assert host.file("/etc/letsencrypt/renewal/cli.ini").contains("key-type = ecdsa")
    assert host.file("/etc/letsencrypt/renewal/cli.ini").contains(
        "elliptic-curve = secp384r1"
    )

    assert host.file("/etc/letsencrypt/renewal/cli.ini").contains("rsa-key-size = 4096")
