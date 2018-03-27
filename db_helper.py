# coding: utf-8
from user import User
import mysql.connector


# 注释：数据库操作

def init():
    connection = mysql.connector.connect(user='root', password='root', database='file_server_db', use_unicode=True)
    cursor = connection.cursor()
    return


def check_create():
    pass


def dispose():
    pass


def find_user_by_username(username):
    # 查询数据库，填充user
    u = User()
    return None


def insert_user(user):
    pass


def remove_user_by_username(username):
    pass
