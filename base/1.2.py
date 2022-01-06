x = { 'a' }
objects = [1, 2, x, 1, 2, x, 3]

result = []
for obj in objects:
    if obj not in result:
        result.append(obj)

print(len(result))