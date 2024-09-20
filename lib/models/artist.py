# lib/models/artist.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    nationality = Column(String, nullable=False)

    albums = relationship("Album", back_populates="artist", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Artist(name={self.name}, genre={self.genre})>"
