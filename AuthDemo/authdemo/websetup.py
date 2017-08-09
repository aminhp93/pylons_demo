"""Setup the SimpleSite application"""
import logging

from authdemo.config.environment import load_environment
from authdemo.model.meta import Session, Base
from authdemo import model

from authkit.users.sqlalchemy_driver import UsersFromDatabase

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup authdemo here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    users = UsersFromDatabase(model)
    print(users, "++++++++++++++++")

    # Create the tables if they don't already exist
    log.info("Creating tables")
    Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
    Base.metadata.create_all(bind=Session.bind)
    log.info("Successfully setup")

    print(dir(users))
    print(users.list_roles())
    print(users.list_users())
    users.role_create('admin')
    users.user_create('aminh', password='minh1234')
    users.user_add_role('aminh',role='admin')

    print(users.list_roles())
    print(users.list_users())
    Session.commit()

