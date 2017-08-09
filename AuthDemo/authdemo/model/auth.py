from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from authdemo.model.meta import Base

class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<auth('%s')" % self.username