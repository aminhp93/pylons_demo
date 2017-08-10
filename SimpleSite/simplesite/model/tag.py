from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import relation

from simplesite.model.meta import Base
# from association import Association


# association_table = Table('association', Base.metadata,
#     Column('video_id', Integer, ForeignKey('video.id')),
#     Column('tag_id', Integer, ForeignKey('tag.id')),
#     useexisting=True
# )

class Association(Base):
    __tablename__ = "association"

    id = Column(Integer, primary_key=True)
    video_id = Column(Integer,ForeignKey('video.id'))
    tag_id = Column(Integer,ForeignKey('tag.id'))
    useexisting = True


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    content = Column(String(100))
    confirm = Column(Boolean, nullable=False, default=False)
    page_id = Column(Integer, ForeignKey('page.id'))
    video = relation("Video",
                    secondary="association",
                    backref="tags")

    def __init__(self, content='', confirm=''):
        self.content = content
        self.confirm = confirm
        

    def __repr__(self):
        return "<Tag('%s')" % self.content


   