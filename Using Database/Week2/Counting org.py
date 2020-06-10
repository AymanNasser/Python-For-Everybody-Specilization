import sqlite3
import re
# Creating a file organization counts
connection = sqlite3.connect('org_counts.sqlite')
# Cursor is kind like a handle
cur = connection.cursor()

# Removing table if exists
cur.execute('DROP TABLE IF EXISTS Counts')
# Creating new table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open('../../../../mbox.txt','r')

for line in fh:
    line = line.strip()
    if not line.startswith('From: '): continue
    pieces = re.findall('@([^ ]*)',line)
    # Checking if pieces is empty list
    if len(pieces) > 0:
        org = pieces[0]
    else:
        continue
    cur.execute('SELECT count FROM Counts where org = ? ', (org,))

    # To retrieve data after executing a SELECT statement, call the cursor’s fetchone() method to retrieve a single
    # matching row, or call fetchall() to get a list of the matching rows.
    row = cur.fetchone()

    # if row is None that means that the specified mail doesn't exist so we insert it
    # else we increment its count
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES(?,1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 where org = ?', (org,))

# committing to the database each iteration
connection.commit()



# Printing elements in the database
temp_str = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(temp_str):
    print(row[0],row[1])