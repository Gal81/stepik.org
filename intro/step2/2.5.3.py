# data = '4 8 0 3 4 2 0 3'
# data = '10'
# data = '1 1 2 2 3 3'
# data = '1 1 1 1 1 2 2 2'
data = [int(i) for i in input().split()]
data = sorted(data)

slice = [data[0]]
result = []
for i in data[1:]:
    if i in slice and i not in result:
        result.append(i)
    else:
        slice = [i]

for i in result:
    print(i, end = ' ')