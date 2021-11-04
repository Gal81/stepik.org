n = int(input())
# n = 3

# games = [
#     'Спартак;9;Зенит;10',
#     'Локомотив;12;Зенит;3',
#     'Спартак;8;Локомотив;15',
# ]

# победа — 3
# поражение — 0
# ничья — 1

results = {}
for i in range(n):
    game = input().split(';')
    # game = games[i].split(';')

    command_1 = game[0]
    score_1 = int(game[1])

    command_2 = game[2]
    score_2 = int(game[3])

    if command_1 not in results:
        results[command_1] = [0, 0, 0, 0, 0]

    if command_2 not in results:
        results[command_2] = [0, 0, 0, 0, 0]

    results[command_1][0] += 1
    results[command_2][0] += 1

    if score_1 == score_2:
        results[command_1][2] += 1
        results[command_1][4] += 1

        results[command_2][2] += 1
        results[command_2][4] += 1

    if score_1 > score_2:
        results[command_1][1] += 1
        results[command_1][4] += 3

        results[command_2][3] += 1

    if score_1 < score_2:
        results[command_1][3] += 1

        results[command_2][1] += 1
        results[command_2][4] += 3

for command, scores in results.items():
    result = ''
    for score in scores:
        result += f'{score} '
    print(f'{command}:{result}'.strip())