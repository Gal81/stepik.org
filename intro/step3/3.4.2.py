from pathlib import Path

data = []
path = Path(__file__).parent  / './data342.txt'
with path.open() as file:
    for line in file:
        data.append(line.strip())

dict = {}
for line in data:
    words = line.split(' ')

    for item in words:
        word = item.lower()
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

max = 0
for value in dict.values():
    if value > max:
        max = value

results = []
for key, value in dict.items():
    if value == max:
        results.append(key)

result = f'{sorted(results)[0]} {max}'
print(result)

pathSave = Path(__file__).parent  / './result342.txt'
with pathSave.open('w') as file:
    file.write(result)