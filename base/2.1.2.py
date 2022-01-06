import json

chain = []
store = []
def get_obj(name):
    global store

    for obj in store:
        if obj['name'] == name:
            return obj

def get_all_parents(parents):
    global store

    all_parents = []
    def walk(items):
        for item in items:
            obj = get_obj(item)
            if obj != None:
                next_parents = obj['parents']
                if next_parents != None:
                    all_parents.extend(next_parents)
                    walk(next_parents)

    walk(parents)
    return list(set(all_parents))

def update_parents(name):
    global store

    obj = get_obj(name)
    if obj != None:
        parents = obj['parents']

        for x in store:
            if (parents != None) and (name in x['parents']):
                x['parents'].extend(parents)

def read_inheritance(str):
    name = ''
    parents = []

    if ':' in str:
        name, rest = str.split(' : ')
        rest = rest.split(' ')
        rest.extend(get_all_parents(rest))
        parents = rest
    else:
        name = str

    store.append({
        'name': name,
        'parents': parents,
    })
    update_parents(name)

def fill_chain(name):
    global chain
    chain.append(name)

def result():
    global chain

    omit = []
    heap = []
    for name in chain:
        item = get_obj(name)

        for parent in heap:
            if (parent in item['parents']) and (name not in omit):
                omit.append(name)
            elif (name in heap) and (name not in omit):
                omit.append(name)

        heap.append(name)

    for item in omit:
        print(item)

def main():
    global store

    n = int(input())
    for _ in range(n):
        read_inheritance(input())

    m = int(input())
    for _ in range(m):
        fill_chain(input())

    # read_inheritance('ArithmeticError')
    # read_inheritance('ZeroDivisionError : ArithmeticError')
    # read_inheritance('OSError')
    # read_inheritance('FileNotFoundError : OSError')

    # fill_chain('ZeroDivisionError')
    # fill_chain('OSError')
    # fill_chain('ArithmeticError')
    # fill_chain('FileNotFoundError')

    result()

    # print(json.dumps(store, indent=4))

main()