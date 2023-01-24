# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Review the variables as shown in defaults.

```
certbot_email: ""
certbot_domains: []

certbot_verbose: false
certbot_dry_run: false
certbot_hooks_enabled: true
```

The ansible playbook will validate whether the variables exist that you defined before running.

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.certbot

```

# TLDR - What will happen if I run this

- run systemd-failmail role, to configure service that can send out mails on failure.
- validate whether rules/some other variables are defined
- install certbot
- install hooks (when requested)
- edit and enable systemd service for certbot

# Future improvements

- Support more type of hooks
