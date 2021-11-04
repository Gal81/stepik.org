from pathlib import Path

data = []
path = Path(__file__).parent  / './data331.txt'
with path.open() as file:
    for line in file:
        data.append(line.strip())

result = []
for line in data:
    row = ''
    num = ''
    for value in reversed(line):
        if value.isnumeric():
            num = f'{value}{num}'
        else:
            row = f'{value * int(num)}{row}'
            num = ''

    result.append(row)
    row = ''

pathSave = Path(__file__).parent  / './result331.txt'
with pathSave.open('w') as file:
    for row in result:
        file.write(row)