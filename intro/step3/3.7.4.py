# n = 4
n = int(input())

# commands = [
#     'север 10',
#     'запад 20',
#     'юг 30',
#     'восток 40',
# ]

coordinates = [0, 0]
for i in range(n):
    # command = commands[i].split(' ')
    command = input().split(' ')
    direction = command[0]
    shift = int(command[1])

    if direction == 'восток':
        coordinates[0] += shift
    if direction == 'запад':
        coordinates[0] -= shift
    if direction == 'север':
        coordinates[1] += shift
    if direction == 'юг':
        coordinates[1] -= shift

print(coordinates[0], coordinates[1])