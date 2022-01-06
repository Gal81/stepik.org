store = []
def get_obj(name):
    global store

    for obj in store:
        if obj['name'] == name:
            return obj

def is_parent(parent, name):
    obj = get_obj(name)
    if obj == None:
        print('No')
    else:
        parents = obj['parents']
        if (parent == name) or (parents != None and parent in parents):
            print('Yes')
        else:
            print('No')

def get_all_parents(parents):
    global store

    all_parents = []
    def walk(items):
        for item in items:
            obj = get_obj(item)
            if obj != None:
                next_parents = obj['parents']
                # print(item, '>>>', next_parents)
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
        # print(name, '>>>', parents)

        for x in store:
            if (parents != None) and (name in x['parents']):
                x['parents'].extend(parents)

def update_store(str):
    if ':' in str:
        name, rest = str.split(':')
        name = name.strip()
        rest = rest.strip().split(' ')
        rest.extend(get_all_parents(rest))
        parents = rest
    else:
        name = str
        parents = []

    store.append({
        'name': name,
        'parents': parents,
    })
    update_parents(name)

def main():
    n = int(input())
    for _ in range(n):
        str = input()
        update_store(str)

    q = int(input())
    for _ in range(q):
        parent, name = input().split(' ')
        is_parent(parent, name)

main()




def test():
    update_store('G : F')
    update_store('A')
    update_store('B : A')
    update_store('C : A')
    update_store('D : B C')
    update_store('E : D')
    update_store('F : D')
    update_store('X')
    update_store('Y : X A')
    update_store('Z : X')
    update_store('V : Z Y')
    update_store('W : V')

    is_parent('A', 'G') # Yes   # A предок G через B/C, D, F
    is_parent('A', 'Z') # No    # Y потомок A, но не Y
    is_parent('A', 'W') # Yes   # A предок W через Y, V
    is_parent('X', 'W') # Yes   # X предок W через Y, V
    is_parent('X', 'QWE') # No    # нет такого класса QWE
    is_parent('A', 'X') # No    # классы есть, но они нет родства :)
    is_parent('X', 'X') # Yes   # родитель он же потомок
    is_parent('1', '1') # No    # несуществующий класс

# test()