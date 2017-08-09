"""The application's model objects"""
from authdemo.model.meta import Session, Base
from authdemo.model.auth import Auth

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
