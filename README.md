# Drupal Migration

## Notes on using `terminus` with Pantheon

### Installation

Follow [installation instructions](https://docs.pantheon.io/terminus/install) with following notes:

- Prerequisite requirements can be skipped if using this development container
- Authentication: both machine token and SSH authentication is needed for full functionality

### Operation

```bash
# Site & development environment
SITE_ENV="<site_name>.<dev_env>"
PANTHEON_USER="<pantheon-user-email>"
PANTHEON_TOKEN="<machine-token>"
DRUPAL_USER="<drupal-user-name>"
```

#### Logging in

```bash
terminus auth:login --email=${PANTHEON_USER} --machine-token=${PANTHEON_TOKEN}
```

#### Pantheon code update mode

```bash
# switch Pantheon code update mode to sftp
terminus connection:set ${SITE_ENV} sftp
```

#### Add administrator role to user

```bash
terminus drush ${SITE_ENV} -- user:information ${DRUPAL_USER}
terminus drush ${SITE_ENV} -- user:role:add administrator ${DRUPAL_USER}
```

#### Install `composer` and `markdown_importer` module

```bash
terminus self:plugin:install pantheon-systems/terminus-composer-plugin
terminus composer ${SITE_ENV} -- require 'league/commonmark'
terminus composer ${SITE_ENV} -- require 'drupal/markdown_importer:^1.0'
```

## Processing Original HTML Files

Using the sitemap URL list, we run the following script:

```sh
python processing.py urllist.txt ./
```

The script does the following:
- Takes in a list of sitemap URL's (`urllist.txt`).
- Takes in a location to dump contents into a `src/` directory containing MD files and `nonhtml/` directory containing site files (e.g. `./` would save in `./src/` and `./nonhtml`).
- Removes the old navigation content up until header 1.
- Adds a header 1 containing the filename/processed url. This is so that Drupal's Markdown Importer imports all MD files without overwriting any. Markdown Importer uses the top header as the page title.
- Removes most of the footer content.
