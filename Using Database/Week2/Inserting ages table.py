import sqlite3
# Creating a file ages
connection = sqlite3.connect('ages.sqlite')
# Cursor is kind like a handle
cur = connection.cursor()

# Removing table if exists
cur.execute('DROP TABLE IF EXISTS Ages')
# Creating new table
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')


cur.execute('DELETE FROM Ages')
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Fares',35))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Jessica',34))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Christoph',32))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Sajjad',39))
connection.commit()

# Executing a specific command for verifying database valid execution
for row in cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X'):
    print(row[0])
