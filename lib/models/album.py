from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Album(Base):
    """defines the album class"""
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    artist = relationship("Artist", back_populates="albums")

    def __repr__(self):
        return f"<Album(title={self.title}, release_year={self.release_year})>"
