size = 5

matrix = [[0] * size for x in range(size)]

num = 0
# stop = size ** 2
stop = 25
for i in range(size):
    for j in range(i, size):
        num += 1
        if num > stop:
            break
        matrix[i][j] = num
        # print(f'>[{i},{j}]', num)
        if j == size - i - 1:
            for x in range(i + 1, size - i):
                num += 1
                if num > stop:
                    break
                matrix[x][j] = num
                # print('>>', num)
                if x == size - i - 1:
                    for y in range(x - 1, i - 1, -1):
                        num += 1
                        if num > stop:
                            break
                        matrix[x][y] = num
                        if y == i:
                            for z in range(size - i - 2, i, -1):
                                num += 1
                                if num > stop:
                                    break
                                matrix[z][y] = num

print()
for row in matrix:
    print(row)
