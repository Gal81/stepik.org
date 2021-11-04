# n = 7
n = int(input())

count = 0
sequence = []
for i in range(1, n + 1):
    if count == n:
        break

    for j in range(0, i):
        if count == n:
            break

        print(i, end=' ')
        count += 1
