# data = '4 -1 9 3'
data = [int(i) for i in input().split()]
sum = 0
for i in data:
    sum += i
print(sum)