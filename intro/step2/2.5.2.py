# data = '1 3 5 6 10'
# data = '10'

data = [int(i) for i in input().split()]
index = 0
for i in data:
    indexLeft = index - 1 if index - 1 >= 0 else len(data) - 1
    indexRight = index + 1 if index + 1 < len(data) else 0
    if len(data) > 1:
        sum = data[indexLeft] + data[indexRight]
    else:
        sum = data[0]
    index += 1
    print(sum, end = ' ')