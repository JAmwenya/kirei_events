import sqlite3
from .artist import Artist
from .album import Album

CONN = sqlite3.connect('music_album.db')
CURSOR = CONN.cursor()

