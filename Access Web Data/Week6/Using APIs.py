import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


address = 'Ann Arbor, MI'

url = service_url + urllib.parse.urlencode({'address' : address})
print(url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print(data)
