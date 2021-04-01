import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
xml = urllib.request.urlopen(url, context=ctx).read()
print('Retrieving', url)
xml = xml.decode()
print('Retrieved', len(xml), 'characters')
xml_parsed = ET.fromstring(xml)
comments_list = xml_parsed.findall('comments/comment')
print('Count: ', len(comments_list))
sum = 0
for item in comments_list:
    sum = sum + int(item.find('count').text)
print('Sum: ', sum)
