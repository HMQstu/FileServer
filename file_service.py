# coding: utf-8

import db_helper
import permission_manager
from file_info import FileInfo
import os


def visible_files_list(role):
    all_files = db_helper.query_all_files()
    result = []
    for f in all_files:
        permission = f.permission
        can_read = permission_manager.has_permission(permission, role, permission_manager.PERMISSION_READ)
        if can_read:
            result.append(f)
    return result


UPLOAD_FOLDER = '/Users/wuhaojie/WorkSpace/Python/FileServer'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'ppt', 'pptx'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def insert_new_file(file_io, user_name, file_permission):
    if not allowed_file(file_io.filename):
        return None
    sec_file_name = file_io.filename
    save_path = os.path.join(UPLOAD_FOLDER, sec_file_name)
    file_io.save(save_path)

    file_info = FileInfo()
    file_info.file_name = sec_file_name
    file_info.file_doc = sec_file_name.rsplit('.', 1)[1]
    file_info.creator = user_name
    file_info.download_count = 0
    file_info.permission = file_permission
    file_info.file_path = save_path
    file_info.file_size = os.path.getsize(save_path)

    db_helper.insert_file_info(file_info)
    return file_info