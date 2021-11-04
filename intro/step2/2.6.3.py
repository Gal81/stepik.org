list = [int(i) for i in input().split()]
x = int(input())

# list = [int(i) for i in '5 8 2 7 8 8 2 4'.split()]
# x = int('8')

if x not in list:
    print('Отсутствует')
else:
    while x in list:
        index = list.index(x)
        print(index, end=' ')
        list[index] = 'x'