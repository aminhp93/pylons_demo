from authkit.permissions import ValidAuthKitUser
is_valid_user = ValidAuthKitUser()
print(dir(is_valid_user), "====================is valid user")
# print(is_valid_user.check())

from authkit.authorize.pylons_adaptors import authorized
