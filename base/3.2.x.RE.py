import re
import sys

# lines = []
# for line in sys.stdin:
#     line = line.rstrip()
#     lines.append(line)

# 3.2.1
# pattern = r'(.*?cat.*?){2,}'

# 3.2.2
# pattern = r'.*?\bcat\b.*?'

# 3.2.3
# pattern = r'(.*?)z(.{3})z(.*?)'

# 3.2.4
# pattern = r'(.*)\\(.*)'

# 3.2.5
# pattern = r'(\b(\w+)\2\b)'

# for line in lines:
#     match = re.match(pattern, line)
#     if match:
#         print(line)

# 3.2.6
# for line in lines:
#     print(re.sub(r'human', 'computer', line))

# 3.2.7
# for line in lines:
#     print(re.sub(r'\ba+\b', 'argh', line, count=1, flags=re.IGNORECASE))

# 3.2.8
# for line in lines:
#     matches = re.findall(r'\b(\w{2,})\b', line)
#     for match in matches:
#         word = f'{match[1]}{match[0]}{match[2:]}'
#         line = re.sub(rf'\b{match}\b', word, line)
#     print(line)


lines = [
    'attraction',
    'buzzzz',
    'aaaaaqqqqqqqbbbbb',
]

# 3.2.9
pattern = r'((\w+)\2)'
for line in lines:
    matches = re.findall(pattern, line)
    while len(matches) != 0:
        line = re.sub(pattern, r'\2', line)
        matches = re.findall(pattern, line)
    print(line)