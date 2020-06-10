import sqlite3

def create_courses_table(file_name):

    # Creating a file users
    connection = sqlite3.connect(file_name)
    # Cursor is kind like a handle
    cur = connection.cursor()

    # Removing table if exists
    cur.execute('DROP TABLE IF EXISTS User')
    cur.execute('DROP TABLE IF EXISTS Course')
    cur.execute('DROP TABLE IF EXISTS Member')

    # Creating tables
    cur.execute('''CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE) 
    ''')

    cur.execute('''CREATE TABLE Course (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE)
    ''')

    # Connector table
    # role ==> 0: student, 1: instructor
    # PRIMARY KEY (user_id, course_id) is a composite primary key which, we'll always have only one unique combination
    # of (user_id, course_id)
    cur.execute('''CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id) )
    ''')
