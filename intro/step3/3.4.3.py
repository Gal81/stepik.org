from pathlib import Path

data = []
# path = Path(__file__).parent  / './data343.txt' # unix
path = Path(__file__).parent  / 'data343.txt' # windows
with path.open(encoding='utf-8') as file:
    sum_math = 0
    sum_phys = 0
    sum_lang = 0
    for line in file:
        grades = line.strip().split(';')
        grades.pop(0)

        sum_math += int(grades[0])
        sum_phys += int(grades[1])
        sum_lang += int(grades[2])

        sum = 0
        for grade in grades:
            sum += int(grade)
        avg = sum / len(grades)
        data.append(avg)

total = f'{sum_math / len(data)} {sum_phys / len(data)} {sum_lang / len(data)}'
print(total)

pathSave = Path(__file__).parent  / './result343.txt'
with pathSave.open('w') as file:
    for grade in data:
        file.write(f'{grade}\n')
    file.write(total)
