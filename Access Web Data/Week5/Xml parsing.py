import xml.etree.ElementTree as ET

# ''' ==> multi-line string
data = \
'''<person> 
    <name>Chuck</name>
    <phone type="int1">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
#print(tree.find('name').text)
#print(tree.find('email').get('hide'))

input = \
'''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''


stuff = ET.fromstring(input)
# Returning a list of parsed trees
lst = stuff.findall('users/user')

for treeItem in lst:
    print(treeItem.find('name').text)
    print(treeItem.find('id').text)
    print(treeItem.get('x'))