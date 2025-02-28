# Notes on using `terminus` with Pantheon

## Installation

Follow [installation instructions](https://docs.pantheon.io/terminus/install) with following notes:

- Prerequisite requirements can be skipped if using this development container
- Authentication: both machine token and SSH authentication is needed for full functionality

## Operation

```bash
# Site & development environment
SITE_ENV="<site_name>.<dev_env>"
PANTHEON_USER="<pantheon-user-email>"
PANTHEON_TOKEN="<machine-token>"
DRUPAL_USER="<drupal-user-name>"
```

### Logging in

```bash
terminus auth:login --email=${PANTHEON_USER} --machine-token=${PANTHEON_TOKEN}
```

### Pantheon code update mode

```bash
# switch Pantheon code update mode to sftp
terminus connection:set ${SITE_ENV} sftp
```

### Add administrator role to user

```bash
terminus drush ${SITE_ENV} -- user:information ${DRUPAL_USER}
terminus drush ${SITE_ENV} -- user:role:add administrator ${DRUPAL_USER}
```

### Install `composer` and `markdown_importer` module

```bash
terminus self:plugin:install pantheon-systems/terminus-composer-plugin
terminus composer ${SITE_ENV} -- require 'league/commonmark'
terminus composer ${SITE_ENV} -- require 'drupal/markdown_importer:^1.0'
```