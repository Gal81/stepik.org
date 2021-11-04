d = int(input())
dict = []
for i in range(d):
    word = input()
    dict.append(word.lower())

l = int(input())
result = set()
for i in range(l):
    row = input()
    for word in row.split(' '):
        if word.lower() not in dict:
            result.add(word.lower())

for word in result:
    print(word)
