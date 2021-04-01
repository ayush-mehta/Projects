import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
for i in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url_list = list()
    for tag in tags:
        url_list.append(tag.get('href', None))
    print(url_list[int(position) - 1])
    url = str(url_list[int(position) - 1])
html = urllib.request.urlopen(url, context=ctx).read()
print(html)
