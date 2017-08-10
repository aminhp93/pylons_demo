from authkit.permissions import ValidAuthKitUser, HasAuthKitRole
from authkit.authorize.pylons_adaptors import authorized
from simplesite.lib.base import BaseController, render

is_valid_user = ValidAuthKitUser()

has_delete_role = HasAuthKitRole(['delete'])
has_admin_role = HasAuthKitRole(['admin'])

def render_signin():
    return render('account/signin.html')