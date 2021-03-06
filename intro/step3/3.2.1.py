def update_dictionary(d, key, value):
    if d.get(key):
        d[key].append(value)
    elif d.get(2 * key):
        d[2 * key].append(value)
    else:
        d[2 * key] = []
        d[2 * key].append(value)

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}