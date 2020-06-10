import sqlite3

# Primary key ==> a way to refer to a particular row so its a unique number
# Foreign key ==> a key that is a starting point of the arrows to another table
# Logical key ==> a unique key that we use to look-up from the outside world, it makes it easy to retrieve data for a
# a specific row

def create_tracks_table(file_name):

    # Creating a file Tracks
    connection = sqlite3.connect(file_name)
    # Cursor is kind like a handle
    cur = connection.cursor()

    # Removing table if exists
    cur.execute('DROP TABLE IF EXISTS Track')
    cur.execute('DROP TABLE IF EXISTS Artist')
    cur.execute('DROP TABLE IF EXISTS Album')
    cur.execute('DROP TABLE IF EXISTS Genre')

    # Creating new Track table
    # Text is a logical key
    # album_id & genre_id are foreign keys
    cur.execute('''CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id TEXT,
    genre_id TEXT, 
    len INTEGER, rating INTEGER, count INTEGER)
    ''')

    # Creating new Artist table
    cur.execute('''CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE)
    ''')


    # Creating new Genre table
    cur.execute('''CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE)
    ''')

    # Creating new Album table
    cur.execute('''CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER, 
    title TEXT UNIQUE)
    ''')

    connection.commit()


