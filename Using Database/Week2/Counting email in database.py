import sqlite3
# Creating a file emaildb
connection = sqlite3.connect('emaildb.sqlite')
# Cursor is kind like a handle
cur = connection.cursor()

# Removing table if exists
cur.execute('DROP TABLE IF EXISTS Counts')
# Creating new table
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fh = open('../../../../mbox.txt','r')

for line in fh:
    line = line.strip()
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # We put ? as a placeholder wherever you want to use a value, and then provide a tuple of values as the second
    # argument to the cursor’s execute() method
    # The question mark (?) is a placeholder to be replaced by tuple (email,)
    cur.execute('SELECT count FROM Counts where email = ? ', (email,))

    # To retrieve data after executing a SELECT statement, call the cursor’s fetchone() method to retrieve a single
    # matching row, or call fetchall() to get a list of the matching rows.
    row = cur.fetchone()

    # if row is None that means that the specified mail doesn't exist so we insert it
    # else we increment its count
    if row is None:
        cur.execute('INSERT INTO Counts (email,count) VALUES(?,1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 where email = ?', (email,))
    # committing to the database each iteration
    connection.commit()


#cur.execute('DELETE FROM Counts where count = 1')
#connection.commit()

# Printing elements in the database
temp_str = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(temp_str):
    print(row[0],row[1])


