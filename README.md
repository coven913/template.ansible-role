# Coven913 Ansible Role Template

This repository provides an opinionated template for ansible roles.

It is mainly intended to be used as a template repository for ansible role repositories, and includes a skeleton file structure, example files, CI/CD workflows for version/release management and configuration files for git.

This repository tries to adhere to RedHat conventions for ansible, and expands on them occasionally. It is heavily opinionated and tailored to the way we do things at Coven913


- [Usage](#usage)
  - [Creating a new ansible role repository from this template:](#creating-a-new-ansible-role-repository-from-this-template)
    - [Use as repository template](#use-as-repository-template)
    - [Manual cloning](#manual-cloning)
    - [Cleanup](#cleanup)
- [versioning](#versioning)
- [Contributing](#contributing)
- [Getting help](#getting-help)
- [License](#license)
- [Authours](#authours)

## Usage

### Creating a new ansible role repository from this template:

#### Use as repository template

To use this repository to create an ansible role repository on github, you can simply [create a new github repository from this template repository.](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

#### Manual cloning

If you want to create your repository locally or on another Git server, you can either fork this repository to your git server and set it up as a repository template there, or clone it, and copy the contents to your project directory. In the latter case, make sure to not copy the contents of `./.git/`

#### Cleanup

After cloning the repository, you should at the very least complete the following cleanup operations:

1. Remove the following files:
   + `./CHANGELOG.md`
   + `./README.md`
2. Rename `role_README.md` to `./README.md`
3. Remove all cursive text in `./README.md` or replace it with actual content.
4. Remove all not commented lines in `./CODEOWNERS`
5. change the version in `./.release-please-manifest.json` to `0.0.0`


## versioning
This repository includes a [release-please](https://github.com/googleapis/release-please-action) configuration that versions an ansible role repository as per internal versioning conventions (documentation will follow).

Since this repository is also versioned using this configuration, please make the following changes after creating a new repository based on this template to ensure versioning works properly:
1. remove `./CHANGELOG.md`
2. change the version in `./.release-please-manifest.json` to `0.0.0`

## Contributing

We are generally open for contributions, but we aim to update this repository as infrequently as possible in order for all repositories created based on it to remain as uniform as possible.

Furthermore, this is an opinionated project which is largely optimized for internal use at Coven913. Therefore, suggetions that don't fix errors, add useful new features or implement upstream updates will likely be rejected.

## Getting help
If you have a problem or suggestion, please [open an issue](https://github.com/coven913/template.ansible-role/issues/new) in this repository, and we will do our best to help.
However, we are under no obligation to respond to support requests and or provide support. Support is merely provided at will.
Please note that this project adheres to the [Contributor Covenant Code of Conduct](/CODE_OF_CONDUCT.md).

## License
This project is licensed under the [AGPL 3.0 License](https://www.gnu.org/licenses/agpl-3.0.en.html)

The AGPL license grant is not for GitHub's trademarks, which include the logo designs. GitHub reserves all trademark and copyright rights in and to all GitHub trademarks.

GitHub® and its stylized versions and the Invertocat mark are GitHub's Trademarks or registered Trademarks. When using GitHub's logos, be sure to follow the GitHub logo guidelines

## Authours
This project was designed and authored by [Valentina Mellar](https://github.com/valiac) for [Coven913](https://github.com/coven913)
see https://github.com/coven913/template.ansible-role/graphs/contributors for a complete list of people who've contributed.