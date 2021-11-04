a = int(input())
b = int(input())
c = int(input())
d = int(input())

# a = 5
# b = 5
# c = 6
# d = 6

for i in range(c, d + 1):
    print(f' \t{i}', end='')
print()

for i in range(a, b + 1):
    print(f'{i}', end='')
    for j in range(c, d + 1):
        print(f'\t{j * i}', end='')
    print()