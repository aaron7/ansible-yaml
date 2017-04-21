from ansible.module_utils.basic import AnsibleModule


def main():
    fields = {
        "path": {"requred": True, "type": "str"},
        "key": {"required": True, "type": "str"},
        "value": {"required": True, "type": "str"},
        "state": {
            "default": "present",
            "choices": ["present", "absent"],
            "type": "str"
        },
        "ordered": {"default": True, "type": "bool"},
    }
    choice_map = {
      "present": yaml_value_present,
      "absent": yaml_value_absent,
    }

    module = AnsibleModule(argument_spec=fields)
    has_changed, result = choice_map.get(module.params['state'])(module.params)
    module.exit_json(changed=has_changed, meta=result)


def yaml_value_present(data):
    has_changed = False
    meta = {"present": "not yet implemented"}
    return (has_changed, meta)


def yaml_value_absent(data=None):
    has_changed = False
    meta = {"absent": "not yet implemented"}
    return (has_changed, meta)


if __name__ == '__main__':
    main()
