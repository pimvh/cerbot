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

# License

The GPLv3 License (GPLv3)

Copyright (c) 2022 Author

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
