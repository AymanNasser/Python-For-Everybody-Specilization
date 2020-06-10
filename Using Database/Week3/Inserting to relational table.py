import sqlite3
import xml.etree.ElementTree as ET
from relational_table import create_tracks_table

create_table('tracks.sqlite')

# Connecting a file Tracks
connection = sqlite3.connect('tracks.sqlite')
# Cursor is kind like a handle
cur = connection.cursor()

def lookup(dict, key):
    found = False
    for child in dict:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None



# Direct parsing a file, not a string like week5 course-3
data = ET.parse('Library.xml')
tracks_list = data.findall('dict/dict/dict')
#print(len(tracks_list))

for track in tracks_list:

    # If no track in this dictionary
    if lookup(track, 'Track ID') is None: continue

    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    genre = lookup(track, 'Genre')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    # Ignore for skipping the specified value if exists

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES(?)',(artist,))
    # Checking if the above inserting occurred or not by retrieving id for current track artist
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES(?,?)', (album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES(?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''
    INSERT OR REPLACE INTO TRACK (title, album_id, genre_id, len, rating, count) VALUES(?,?,?,?,?,?)
    ''', (name,album_id,genre_id,length,rating,count))

connection.commit()

cur.execute('''
SELECT Track.title, Genre.name , Artist.name, Album.title FROM Track JOIN Genre JOIN Artist JOIN Album
ON Track.genre_id = Genre.id and Album.artist_id = Artist.id and Track.album_id = Album.id 
''')
connection.commit()


for row in cur.execute('SELECT id, title, album_id, genre_id FROM Track ORDER BY id ASC'):
    print('ID: ',row[0],'Title: ',row[1],'Album: ',row[2],'Genre: ',row[3])