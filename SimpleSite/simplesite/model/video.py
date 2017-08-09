from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation

from simplesite.model.meta import Base

class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    url = Column(String(100))
    page_id = Column(Integer, ForeignKey('page.id'))
    tag = relation("Tag",
                    secondary="association",
                    backref="videos")

    def __init__(self, title='', url=''):
        self.title = title
        self.url = url

    def __repr__(self):
        return "<Video('%s')" % self.title
