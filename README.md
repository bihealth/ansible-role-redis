[![Build Status](https://travis-ci.org/bihealth/ansible-role-redis.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-redis)

# Setup of Redis

This Ansible role performs a basic single-node Redis setup (the focus is Django apps at the moment).

## Requirements

none

## Role Variables

none

## Dependencies

none

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: bihealth.redis
```

## License

MIT

## Author Information

- Manuel Holtgrewe

Created with love at [CUBI](https://www.cubi.bihealth.org).
