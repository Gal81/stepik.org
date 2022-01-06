namespaces = []

def get_namespace(namespace):
    global namespaces

    for item in namespaces:
        if item['name'] == namespace:
            return item

def create_namespace(namespace, parent):
    global namespaces

    namespaces.append({
        'name': namespace,
        'vars': set(),
        'parent': parent,
    })

def add_to_namespace(namespace, var):
    global namespaces

    space = get_namespace(namespace)
    if space == None:
        vars = set()
        vars.add(var)
        namespaces.append({
            'name': namespace,
            'vars': vars,
            'parent': None,
        })
    else:
        space['vars'].add(var)

def get_namespace_name(namespace, var):
    name = None
    def walk(space):
        nonlocal name

        if space and name == None:
            if var in space['vars']:
                name = space['name']
            else:
                walk(get_namespace(space['parent']))

    walk(get_namespace(namespace))
    print(name)

def parse_row(row):
    command, namespace, var = row.split(' ')

    if command == 'create':
        create_namespace(namespace, var)

    if command == 'add':
        add_to_namespace(namespace, var)

    if command == 'get':
        get_namespace_name(namespace, var)

def main():
    # n = int(input())
    # i = 0
    # while i < n:
    #     parse_row(input())
    #     i += 1

    parse_row('add global a')
    parse_row('create foo global')
    parse_row('add foo b')
    parse_row('get foo a')
    parse_row('get foo c')
    parse_row('create bar foo')
    parse_row('add bar a')
    parse_row('get bar a')
    parse_row('get bar b')

main()