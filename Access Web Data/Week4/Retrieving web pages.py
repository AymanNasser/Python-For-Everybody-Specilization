import urllib.request, urllib.parse, urllib.error

# Retrieving data(romeo.txt document) from a web page & returns a file handle to process on
# Instead of open()
#file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
file_handle = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in file_handle:
    print(line.decode().strip())