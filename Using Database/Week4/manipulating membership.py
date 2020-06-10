import sqlite3
from roster import create_courses_table
import json

create_courses_table('membershipdb.sqlite')

# connecting to membership file
connection = sqlite3.connect('membershipdb.sqlite')
# Cursor is kind like a handle
cur = connection.cursor()

json_file = open('roster_data.json').read()
data = json.loads(json_file)

for item in data:

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES(?)', (item[0],))
    cur.execute('SELECT id FROM User WHERE name = ? ', (item[0], ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (name) VALUES(?)', (item[1],))
    cur.execute('SELECT id FROM Course WHERE name = ? ', (item[1], ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES(?,?,?)',(user_id,course_id,item[2]))

connection.commit()








