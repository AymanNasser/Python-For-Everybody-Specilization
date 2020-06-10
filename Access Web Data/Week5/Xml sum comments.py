import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


file_handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_642250.xml').read()

tree = ET.fromstring(file_handle)
print(tree)
comment_list = tree.findall('comments/comment')
accum = 0
for comment in comment_list:
    #print(comment.find('name').text)
    accum = accum + int(comment.find('count').text)

print(len(comment_list))
print(accum)