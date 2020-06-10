import json

data = \
'''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
# info is a dictionary
info = json.loads(data)
print('name', info['name'])
print('phone',info['phone'])
print(info['email']['hide'])


input = \
'''[
{ 
    "id" : "001",
    "x" : "2",
    "name" : "Chuck"
},
{ 
    "id" : "009",
    "x" : "7",
    "name" : "Brent"
}
]'''

info = json.loads(input)

for items in info:
    print('name', items['name'])
    print('id', items['id'])


