import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

params = {}
api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'

address = 'Lviv University'

params['address'] = address
params['key'] = api_key
url = service_url + urllib.parse.urlencode(params)
print('retrieving URL',url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
data = json.loads(data)

print(data['results'][0]['place_id'])