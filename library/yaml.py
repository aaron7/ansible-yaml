from ansible.module_utils.basic import AnsibleModule
import yaml


def main():
    fields = {
        'path': {'requred': True, 'type': 'str'},
        'key': {'required': True, 'type': 'str'},
        'value': {'required': False, 'type': 'str'},
        'state': {
            'default': 'present',
            'choices': ['present', 'absent'],
            'type': 'str'
        },
        'sort': {'default': False, 'type': 'bool'},
    }

    module = AnsibleModule(argument_spec=fields)
    path = module.params['path']
    key = module.params['key']
    value = module.params['value']
    state = module.params['state']
    sort = module.params['sort']

    has_changed, result = do_yaml(module, path, key, value, state, sort)
    module.exit_json(changed=has_changed, meta=result)


def do_yaml(module, path, key, value, state, sort):
    with open(path, 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            return {False, {'error': 'Failed to parse yaml file'}}

    # Get items using key (the value returned is a reference)
    items = traverse_key(data, key)
    has_changed = False

    # Update state
    if state == 'present':
        if value not in items:
            items.append(value)
            has_changed = True
    elif state == 'absent':
        if value in items:
            items.remove(value)
            has_changed = True

    # Possibly sort
    if sort:
        items_before = items[:]
        items.sort()
        if items != items_before:
            has_changed = True

    if has_changed:
        save_yaml(data, path)

    return (has_changed, {})


def traverse_key(data, key):
    def _traverse_list_key(data, list_key):
        if len(list_key) == 1:
            return data[key]
        else:
            return _traverse_list_key(data[list_key[0]], list_key[1:])

    if isinstance(key, str):
        return _traverse_list_key(data, [key])
    elif isinstance(key, list):
        return _traverse_list_key(data, key)
    raise Exception("Invalid key")


def save_yaml(data, path):
    with open(path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


if __name__ == '__main__':
    main()
