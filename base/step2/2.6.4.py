# data = [
#     [9, 5, 3],
#     [0, 7, -1],
#     [-5, 2, 9],
# ]

# data = [[1]]

data = []
while True:
    raw = input()
    if raw == 'end':
        break

    row = [int(i) for i in raw.split()]
    data.append(row)

for i in range(len(data)):
    row = []
    for j in range(len(data[i])):
        left = j - 1 if j - 1 >= 0 else len(data[i]) - 1
        top = i - 1 if i - 1 >= 0 else len(data) - 1
        right = j + 1 if j + 1 < len(data[i]) else 0
        bottom = i + 1 if i + 1 < len(data) else 0

        sum = data[i][left] + data[top][j] + data[i][right] + data[bottom][j]
        # print('>>', data[i][left], data[top][j], data[i][right], data[bottom][j])
        print(sum, end = ' ')

    print()