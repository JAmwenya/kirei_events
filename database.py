#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///music_album.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Importing the models
    from models.artist import Artist
    from models.album import Album

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Creating the database...")
    init_db()
    print("Database created successfully!")