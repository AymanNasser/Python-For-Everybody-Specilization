import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

init_href = 'http://py4e-data.dr-chuck.net/comments_642248.html'

# Reads the whole file a one string as .read()
def scarpping(url_name):
    soup = None
    try:
        html_parser = urllib.request.urlopen(url_name,context=ctx).read()
    except:
        print('Could not find the specified URL')
        return soup

    soup = BeautifulSoup(html_parser, 'html.parser')
    return soup
accum = 0
soup = scarpping(init_href)
if soup != None:
    # Give us the anchor tag ==> <span> _____ <\span>
    tags = soup('span')
    for tag in tags:
        print(tag)
        tempList = re.findall('[0-9]+', tag.decode())
        accum = accum + sum(list(map(int, tempList)))

else:
    print('Error')

print(accum)
