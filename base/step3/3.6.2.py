import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

def get_next(name, text):
    if name == 'We':
        print(text)

    else:
        data = requests.get(url + name)
        next = data.text.split(' ')[0].strip()
        print('next', next)
        get_next(next, data.text)

get_next('699991.txt', '>>>')