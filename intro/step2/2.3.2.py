a = int(input())
b = int(input())

count = 0
sum = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        sum += i

print(sum / count)
