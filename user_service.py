# coding: utf-8

import db_helper


def query_user(username, password):
    user = db_helper.find_user_by_username(username)
    if user is None:
        # 用户不存在
        return None
    if password != user.password:
        # 密码错误
        return None
    return user


def register_user(user):
    old_user = db_helper.find_user_by_username(user.username)
    if old_user is not None:
        db_helper.remove_user_by_username(user.username)
    db_helper.insert_user(user)
