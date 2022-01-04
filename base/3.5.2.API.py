import requests

client_id = 'ab5a0f48fdd192f81d13'
client_secret = 'e13243ef30bb46d8df4c3b465030440a'

# инициируем запрос на получение токена
params = {
    "client_id": client_id,
    "client_secret": client_secret
}
response = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=params)

# разбираем ответ сервера
j = response.json()

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

ids = [
    '53208af2b202a3a1f900003c',
    '4f5f64c13b555230ac000007',
    '4f5f64c13b555230ac000001',
    '542e86e47261695773da1700',
    '55f0747b7261693808000030',
    '515b144305635113a5000b81',
    '511294005c85615a61000082',
    '52aa13959c18dbddef00024b',
    '4f86f41a24907b0001000d46',
    '52840714275b2442c8000150',
    '4f5f64c13b555230ac000003',
    '53e0f86b7261692d77b90000',
    '515b34a9223afaab8f000905',
    '554a788f726169251a210800',
    '4df6938bbc3cf100010007cc',
]

results = []
for id in ids:
    # инициируем запрос с заголовком
    response = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)
    response.encoding = 'utf-8'
    data = response.json()

    # разбираем ответ сервера
    results.append({
        "name": data['sortable_name'],
        "birthday": int(data['birthday']),
    })

results = sorted(results, key=lambda d: (d['birthday'], d['name']))
for row in results:
    # print(row['name'], row['birthday'])
    print(row['name'])

