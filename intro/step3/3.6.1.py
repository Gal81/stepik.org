import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/833.txt'
data = requests.get(url)
data = data.text.splitlines()
# data = list(filter(lambda row: row != '' and row != '***', data))

# print(data)
print()
print('>>>', len(data))
# print('>>>', data.count('\n'))