# coding: utf-8
import db_helper


def download_count_add(file_id):
    file_info = db_helper.find_file_by_id(file_id)
    file_info.download_count = file_info.download_count + 1
    db_helper.update_file_by_id(file_id, file_info)
