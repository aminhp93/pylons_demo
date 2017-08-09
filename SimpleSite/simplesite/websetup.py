"""Setup the SimpleSite application"""
import logging

from simplesite.config.environment import load_environment
from simplesite.model.meta import Session, Base
from simplesite import model

from authkit.users.sqlalchemy_driver import UsersFromDatabase

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
	"""Place any commands to setup simplesite here"""
	# Don't reload the app if it was loaded under the testing environment
	load_environment(conf.global_conf, conf.local_conf)

	users = UsersFromDatabase(model)
	print(users, "============")
	
	# Create the tables if they don't already exist
	log.info("Creating tables")
	Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
	Base.metadata.create_all(bind=Session.bind)
	log.info("Successfully setup")

	log.info("Adding roles and uses...")

	users.role_create("admin")
	users.role_create("delete")
	users.user_create("amin", password="minh1234")
	users.user_create("amin2", password="minh1234")
	users.user_add_role("amin", role="admin")
	users.user_add_role("amin", role="delete")
	print(users, "=========================")
	print(dir(users))
	print(dir(users.list_roles))

	log.info("Adding tags...")
	Session.commit()

