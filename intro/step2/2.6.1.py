# nums = '1 -3 5 -6 -10 13'

sum = 0
nums = []
while True:
    num = int(input())
    nums.append(num)

    sum += num
    if sum == 0:
        break

sum = 0
for num in nums:
    sum += num ** 2

print(sum)