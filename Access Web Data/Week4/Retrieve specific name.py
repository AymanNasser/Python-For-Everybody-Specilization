import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

init_href = 'http://py4e-data.dr-chuck.net/known_by_Andreas.html'

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

count = 7
pos = 18

soup = scarpping(init_href)
if soup != None:
    # Give us the anchor tag ==> <span> _____ <\span>
    tags = soup('a')

    for counter in range(count-1):
        soup = scarpping(tags[pos-1].get('href',None))
        tags = soup('a')


    tempList = tags[pos-1].get('href',None).split('_')
    tempList = tempList[-1].split('.')
    print(tempList[0])

else:
    print('Error')


