from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation

from simplesite.model.meta import Base

class Page(Base):
    __tablename__ = "page"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(100))
    videos = relation('Video', backref='page')
    tags = relation('Tag', backref='page')

    def __init__(self, title='', content=''):
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Page('%s')" % self.title