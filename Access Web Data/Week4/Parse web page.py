import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

init_href = 'http://dr-chuck.com'

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

soup = scarpping(init_href)
if soup != None:
    # Give us the anchor tag ==> <a> _____ <\a>
    tags = soup('a')
    for tag in tags:
        print(tag)
        print(tag.get('href',None))
