from authkit.permissions import ValidAuthKitUser, HasAuthKitRole
from authkit.authorize.pylons_adaptors import authorized

is_valid_user = ValidAuthKitUser()

has_delete_role = HasAuthKitRole(['delete'])
has_admin_role = HasAuthKitRole(['admin'])

