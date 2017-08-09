"""The application's model objects"""
from simplesite.model.meta import Session, Base
from simplesite.model.page import Page
from simplesite.model.video import Video
from simplesite.model.account import Account

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
