# coding: utf-8

import permission_manager


def parse(file_info, role):
    info = SimpleFileInfo()
    info.file_id = file_info.file_id
    info.file_name = file_info.file_name
    info.file_size = file_info.file_size
    info.creator = file_info.creator
    info.created_at = file_info.created_at
    info.file_doc = file_info.file_doc
    info.download_count = file_info.download_count
    code = file_info.permission
    info.can_see = permission_manager.has_permission(code, role, permission_manager.PERMISSION_READ)
    info.can_download = permission_manager.has_permission(code, role, permission_manager.PERMISSION_DOWNLOAD)
    info.can_delete = permission_manager.has_permission(code, role, permission_manager.PERMISSION_DELETE)
    return info


class SimpleFileInfo:

    def __init__(self):
        self.file_id = 0
        self.file_name = ''
        self.file_size = 0
        self.creator = ''
        self.created_at = 0
        self.file_doc = ''
        self.download_count = 0
        self.can_see = True
        self.can_download = True
        self.can_delete = False
