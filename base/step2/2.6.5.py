# size = int(input())
size = 5

matrix = [[0] * size for x in range(size)]

num = 0
def fill_cell(x, y):
    global num
    num += 1
    matrix[x][y] = num

for i in range((size // 2 + size % 2)):
    for j in range(i, size - i):
        fill_cell(i, j)

    for j in range(i + 1, size - i):
        fill_cell(j, size - i - 1)

    for j in range(size - i - 2, i - 1, -1):
        fill_cell(size - i - 1, j)

    for j in range(size - i - 2, i, -1):
        fill_cell(j, i)

print()
for row in matrix:
    for cell in row:
        print(cell, end=' ')
    print()
