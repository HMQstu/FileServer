# coding: utf-8

import db_helper
import permission_manager
from file_info import FileInfo
import os


def drop_file(file_id, role):
    file_info = db_helper.find_file_by_id(file_id)
    if file_info is None:
        return -1
    permission_code = file_info.permission
    has_permission = permission_manager.has_permission(permission_code, role, permission_manager.PERMISSION_DELETE)
    if not has_permission:
        return -3
    db_helper.drop_file_by_id(file_id)
    return 0


def visible_files_list(role):
    all_files = db_helper.query_all_files()
    result = []
    for f in all_files:
        permission = f.permission
        can_read = permission_manager.has_permission(permission, role, permission_manager.PERMISSION_READ)
        if can_read:
            result.append(f)
    return result


UPLOAD_FOLDER = 'F:\humengqiu\workpace\FileServer'
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
