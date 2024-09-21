from lib.models.artist import Artist
from lib.models.album import Album
from lib.database import SessionLocal

# exit the program
def exit_program():
    print("Goodbye!")
    exit()

# creating an Artist
def create_artist():
    session = SessionLocal()
    name = input("Enter artist name: ")
    genre = input("Enter artist genre: ")
    nationality = input("Enter artist nationality: ")

    new_artist = Artist(name=name, genre=genre, nationality=nationality)
    session.add(new_artist)
    session.commit()
    print(f"Artist {name} added successfully!")
    session.close()

# listing the artists in the database
def list_artists():
    session = SessionLocal()
    artists = session.query(Artist).all()
    if artists:
        for artist in artists:
            print(f"ID: {artist.id}, Name: {artist.name}, Genre: {artist.genre}, Nationality: {artist.nationality}")
    else:
        print("No artists found.")
    session.close()

# deleting an artist
def delete_artist():
    session = SessionLocal()
    artist_id = input("Enter the artist ID to delete: ")
    artist = session.query(Artist).filter_by(id=artist_id).first()
    if artist:
        session.delete(artist)
        session.commit()
        print(f"Artist {artist.name} deleted successfully!")
    else:
        print("Artist not found.")
    session.close()

# creating an Album
def create_album():
    session = SessionLocal()
    title = input("Enter album title: ")
    release_year = int(input("Enter release year: "))
    artist_id = int(input("Enter artist ID: "))

    artist = session.query(Artist).filter_by(id=artist_id).first()
    if not artist:
        print(f"Artist with ID {artist_id} not found.")
        session.close()
        return

    new_album = Album(title=title, release_year=release_year, artist_id=artist.id)
    session.add(new_album)
    session.commit()
    print(f"Album {title} added successfully to artist {artist.name}!")
    session.close()

# listing the albums in the database
def list_albums():
    session = SessionLocal()
    albums = session.query(Album).all()
    if albums:
        for album in albums:
            artist = album.artist
            print(f"Album ID: {album.id}, Title: {album.title}, Year: {album.release_year}, Artist: {artist.name}")
    else:
        print("No albums found.")
    session.close()

# deleting an album
def delete_album():
    session = SessionLocal()
    album_id = input("Enter the album ID to delete: ")
    album = session.query(Album).filter_by(id=album_id).first()
    if album:
        session.delete(album)
        session.commit()
        print(f"Album {album.title} deleted successfully!")
    else:
        print("Album not found.")
    session.close()

# updating an album
def update_album():
    session = SessionLocal()
    album_id = input("Enter the album ID to update: ")
    album = session.query(Album).filter_by(id=album_id).first()
    if album:
        title = input(f"Enter new title for album {album.title}: ")
        release_year = int(input(f"Enter new release year for album {album.title}: "))
        artist_id = int(input(f"Enter new artist ID for album {album.title}: "))

        artist = session.query(Artist).filter_by(id=artist_id).first()
        if not artist:
            print(f"Artist with ID {artist_id} not found.")
            session.close()
            return

        album.title = title
        album.release_year = release_year
        album.artist_id = artist.id
        session.commit()
        print(f"Album {title} updated successfully!")
    else:
        print("Album not found.")
    session.close