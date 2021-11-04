def f(x):
    pass

dict = {}
i = 0
n = int(input())
while i < n:
    num = int(input())
    if num in dict:
        print(dict[num])
    else:
        dict[num] = f(num)
        print(dict[num])
    i += 1