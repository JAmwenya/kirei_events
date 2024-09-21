import sqlite3
from .artist import Artist
from .album import Album

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

