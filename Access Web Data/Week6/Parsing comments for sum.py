import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


temp = 'http://py4e-data.dr-chuck.net/comments_642251.json'
url = urllib.request.urlopen(temp, context=ctx)

uh = url.read().decode()
data = json.loads(uh)
accum = 0

for items in data['comments']:
    accum = accum + items['count']

print(accum)