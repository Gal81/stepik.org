import os

result = []
for current_dir, dirs, files in os.walk('base\\dump\\main'):
    has_py = False
    for file in files:
        if file.endswith('.py'):
            has_py = True

    if has_py:
        dir = current_dir.replace('base\\dump\\', '').replace('\\', '/')
        result.append(dir)

with open('base\\dump\\answer.txt', 'a') as answer:
    answer.write('\n'.join(result))