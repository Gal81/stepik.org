# import json
import requests

numbers = []
with open('base\\dump\\dataset_24476_3.txt', 'r') as file:
    numbers = file.read().strip().split('\n')

for num in numbers:
    url = f'http://numbersapi.com/{num}/math?json=true'

    try:
        response = requests.get(url)
        data = response.json()

        if data['found']:
            print('Interesting')
        else:
            print('Boring')
    except Exception:
        print(Exception)