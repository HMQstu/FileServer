# coding: utf-8
from file_info import FileInfo
from user import User
import mysql.connector

connection = None
cursor = None


def init():
    global connection
    connection = mysql.connector.connect(user='root', password='root', database='file_server_db', use_unicode=True)
    global cursor
    cursor = connection.cursor()
    check_create()


def check_create():
    sql = '''
        create table if not exists `user`(
            id bigint primary key auto_increment,
            username varchar(255),
            password varchar(255),
            role int,
            mail varchar(40),
            phone varchar(15)
        );
    '''
    global cursor
    cursor.execute(sql)


def dispose():
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()


def find_user_by_username(username):
    sql = "select username,password,role,mail,phone from `user` where username='%s'" % username
    global cursor
    cursor.execute(sql)
    values = cursor.fetchall()
    for username, password, role, mail, phone in values:
        u = User()
        u.username = username
        u.password = password
        u.role = role
        u.mail = mail
        u.phone = phone
        return u
    return None


def insert_user(user):
    sql = "insert into `user`(id,username,password,role,mail,phone) values(0,'%s','%s',%d,'%s','%s')" \
          % (user.username, user.password, user.role, user.mail, user.phone)
    global cursor
    cursor.execute(sql)
    connection.commit()


def remove_user_by_username(username):
    sql = 'delete from `user` where username = %s' % username
    global cursor
    cursor.execute(sql)
    connection.commit()


def query_all_files():
    sql = ''
    global cursor
    cursor.execute(sql)
    values = cursor.fetchall()
    result = []
    for x in values:
        f = FileInfo()
        result.append(f)
    return result


def insert_file_info(file_info):
    sql = ''
    global cursor
    cursor.execute(sql)
    connection.commit()
