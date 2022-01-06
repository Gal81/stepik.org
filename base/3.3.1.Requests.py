import re
import requests

# linkStart = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# linkEnd = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

linkStart = input()
linkEnd = input()

pattern = r'(?P<url>https?://[^\s\"]+)'
content = requests.get(linkStart)
urls = re.findall(pattern, content.text)

pathFound = False
for url in urls:
    if pathFound == False:
        try:
            content = requests.get(url)
            pathFound = content.status_code == 200 and (linkEnd in content.text)
        except:
            pass

if pathFound:
    print('Yes')
else:
    print('No')