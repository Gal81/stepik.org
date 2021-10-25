num = input()
# num = '123456'

left = int(num[0:1]) + int(num[1:2]) + int(num[2:3])
right = int(num[3:4]) + int(num[4:5]) + int(num[5:6])

if left == right:
    print('Счастливый')
else:
    print('Обычный')