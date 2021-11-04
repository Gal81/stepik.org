from pathlib import Path

height = {}
# result = {}
for i in range(1, 12):
    height[i] = []
    # result[i] = []

# path = Path(__file__).parent  / './data375.tsv' # unix
path = Path(__file__).parent  / 'data375.tsv' # windows
with path.open(encoding='utf-8') as file:
    for line in file:
        data = line.strip().split('\t')
        index = int(data[0])
        value = int(data[2])
        height[index].append(value)

for key, value in height.items():
    if len(value) == 0:
        height[key] = '-'
    else:
        sum = 0
        for num in value:
            sum += num
        height[key] = sum / len(value)

pathSave = Path(__file__).parent  / './result375.txt'
with pathSave.open('w') as file:
    for key, value in height.items():
        file.write(f'{key} {value}\n')