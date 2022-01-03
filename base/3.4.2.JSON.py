import json

data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# data = input()
data = json.loads(data)

def get_parents(name):
    for item in data:
        if item['name'] == name:
            return item['parents']

def get_all_parents(parents):
    all_parents = list(parents)
    def walk(items):
        for name in items:
            next_parents = get_parents(name)
            all_parents.extend(next_parents)
            walk(next_parents)

    walk(parents)
    return list(set(all_parents)) if len(all_parents) != 0 else []

def update_parents():
    for item in data:
        item['parents'] = get_all_parents(item['parents'])

def main():
    update_parents()

    result = {}
    for item in data:
        key = item['name']
        if key not in result:
            result[key] = 1
        else:
            result[key] += 1

        for parent in item['parents']:
            if parent not in result:
                result[parent] = 1
            else:
                result[parent] += 1

    for parent in sorted(result):
        print(f'{parent} : {result[parent]}')

main()