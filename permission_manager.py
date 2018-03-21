# coding: utf-8

BASE_FLAG = 0x01

PERMISSION_READ = BASE_FLAG << 0
PERMISSION_DELETE = BASE_FLAG << 1
PERMISSION_DOWNLOAD = BASE_FLAG << 2
PERMISSION_NULL = BASE_FLAG << 3

ROLE_ADMIN = 0
ROLE_LEADER = 4
ROLE_NORMAL = 8

NORMAL_FILE_PERMISSION = ((PERMISSION_DELETE | PERMISSION_DOWNLOAD | PERMISSION_READ | PERMISSION_NULL) << ROLE_ADMIN) \
                         | ((PERMISSION_READ | PERMISSION_DOWNLOAD | PERMISSION_NULL) << ROLE_LEADER) \
                         | ((PERMISSION_READ | PERMISSION_DOWNLOAD) << ROLE_NORMAL)


def has_permission(code, role, permission):
    return code & (permission << role) == (permission << role)


def set_permission(code, role, permission):
    return code | (permission << role)

# 用法
# f = 0
# f = set_permission(f, ROLE_ADMIN, PERMISSION_READ | PERMISSION_DELETE | PERMISSION_DOWNLOAD)
# f = set_permission(f, ROLE_LEADER, PERMISSION_READ | PERMISSION_DOWNLOAD)
# f = set_permission(f, ROLE_NORMAL, PERMISSION_READ)
#
# b = has_permission(f, ROLE_NORMAL, PERMISSION_DOWNLOAD)
# print(b)
