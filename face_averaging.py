import urllib, urllib2
import re

# Scrape images from online
name = 'adam'
url = 'http://www.famousfix.com/list/celebrities-with-first-name-adam'
response = urllib2.urlopen(url)
html = response.read().decode("utf8")
image_urls = re.findall(r'\ssrc="([^"]+)"', html)

urls =  [url for url in image_urls if '.jpg?' in url]
index = 0
for url in urls:
    urllib.urlretrieve(url, 'images/' + name + str(index) + '.jpg')
    index += 1
