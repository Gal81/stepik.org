import re
import requests

html = '''
    <a href="http://stepic.org/courses">
    <a href='https://stepic.org'>
    <a href='http://neerc.ifmo.ru:1345'>
    <a href="ftp://mail.ru/distib" >
    <a href="ya.ru">
    <a href="www.ya.ru">
    <a href="../skip_relative_links">
'''

link = 'http://pastebin.com/raw/7543p0ns'
# link = input()
html = requests.get(link)

patternUrl = r'<a.+href=[\'\"]?\w[\w:\-\./]+[\'\"]?'
patternHostHead = r'<a.+href=[\'|\"]?((ftp|http|https):/{2})?' # FIXME: find better regex
patternHostTail = r'([/:][\w\d\-\.\'\"]+|[\'\"/+])?'
urls = re.findall(patternUrl, html.text)

hosts = set()
for url in urls:
    host = re.sub(patternHostHead, '', url)
    host = re.sub(patternHostTail, '', host)
    hosts.add(host)

for host in sorted(hosts):
    print(host)
