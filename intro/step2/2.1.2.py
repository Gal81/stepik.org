a = int(input())
b = int(input())
div = 1

while (div % a != 0) or (div % b != 0):
    div += 1

print(div)
