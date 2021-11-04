text = input().split(' ')
# text = 'a aa abC aa ac abc bcd a'.split(' ')

dict = {}
for w in text:
    word = w.lower()
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for key, value in dict.items():
    print(key, value)
