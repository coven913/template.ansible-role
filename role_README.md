# Ansible Role: `<your role>`

_Describe the purpose of your role in 1 sentence_

To include this role in your ansible repository, add the following to  `./requirements.yml` in your repository:

```yaml
- name: <role-name>
  src: <git remote string>
  version: <version>
```

# Description

_explain what your role does short and concise_

## Dependencies

###### Ansible Roles
+ _list any roles your role depends on here, including those specified in ./meta/main.yml_

###### python packages
+ _list any python packages your role depends on here, including those specified in .requirements.txt_

###### custom ansible modules
+ _list any required costum modules that are not included in ./library here_

## Requirements

+ _list any other requirements here_

## Usage

_explain in detail how and when your role should or should not be used and describe all functions and common use cases._

## Role Variables

_Specify all variables this role accepts here using the provided example table format._
_Sub-sections and table columns that are not required may be ommitted._

_For complex structured variables, a codeblock outlining the schema and a separate table with variable descriptions should be added:_

Schema for example_var:

```yaml
example_var:
  - a_value:
    a_list:
      -
    a_list_of_dicts:
      - a_value:
        another_value:
```

#### feature switches

_describe variables which are used to influence the behaviour of the entire role_

Variable | Type | Required | Default | Description/purpose
--- | --- | --- | --- | ---


#### group vars

_describe variables to be specified per host group here. In a simple use cases, most variables go here_

Variable | Type | Required | Default | Description/purpose
--- | --- | --- | --- | ---


#### Host vars

_If your role takes variables which are to be specified uniquely for each host in a group as opposed to the entire target host group, describe them here. A typical use case for this would be a role configuring a cluster, where some settings are to be applied to the entire cluster, and others differ per cluster node._

Variable | Type | Required | Default | Description/purpose
--- | --- | --- | --- | ---

## Example Playbook

_provide an example of how to implement this role in a playbook. provide multiple examples if use cases differ largely_

```yaml
- name: execute my role
  hosts: <group of hosts>
  gather_facts: true
  roles:
    - role: my_role
```