# YAML ansible module

This is a simple ansible module to make it easier to edit YAML files. Created for use in some of my ansible playbooks.

## Installation

Copy `library/yaml.yaml` to the library folder for your playbook.

## Examples

```yaml
- name: Add entry to yaml file
  yaml:
    path: /path/to/file.yml
    key: ingredients
    value: flour

- name: Sort entries in yaml file
  yaml:
    path:  /path/to/file.yml
    key: ingredients
    sort: True

- name: Use key path
  yaml:
    path: /path/to/file.yml
    key: ["cake", "ingredients"]
    value: flour
    sort: True

- name: Remove entry
  yaml:
    path: /path/to/file.yml
    key: "ingredients"
    value: milk
    state: absent
```
