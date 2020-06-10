import re
fh = open('../../romeo.txt','r')
accum = 0

# Program that extract all digits from text & convert extracted string(digits) to ints
for line in fh:
    line = line.strip()

    tempList = re.findall('[0-9]+',line)
    accum = accum + sum(list(map(int,tempList)))

print(accum)