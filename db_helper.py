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
        create table if not exists `files`(
            id bigint primary key auto_increment,
            file_name varchar(255),
            file_size bigint,
            creator varchar(255),
            file_path varchar(255),
            file_doc varchar(40),
            permission int,
            download_count int
        );
    '''
    global cursor
    cursor.execute(sql, multi=True)


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
    sql = "select id,file_name,file_size,creator,file_path,file_doc,permission,download_count from `files`"
    global cursor
    cursor.execute(sql)
    values = cursor.fetchall()
    result = []
    for file_id, file_name, file_size, creator, file_path, file_doc, permission, download_count in values:
        f = FileInfo()
        f.file_id = file_id
        f.file_name = file_name
        f.file_size = file_size
        f.creator = creator
        f.file_path = file_path
        f.file_doc = file_doc
        f.permission = int(permission)
        f.download_count = download_count
        result.append(f)
    return result


def insert_file_info(file_info):
    sql = "insert into `files`(id,file_name,file_size,creator,file_path,file_doc,permission,download_count) " \
          "values(0, '%s', %d, '%s', '%s', '%s', %d, %d)" \
          % (file_info.file_name, file_info.file_size, file_info.creator, file_info.file_path, file_info.file_doc,
             file_info.permission, file_info.download_count)
    global cursor
    cursor.execute(sql)
    connection.commit()


def find_file_by_id(file_id):
    sql = "select id,file_name,file_size,creator,file_path,file_doc,permission,download_count from `files` where id=%d" \
          % file_id
    global cursor
    cursor.execute(sql)
    values = cursor.fetchall()
    for file_id, file_name, file_size, creator, file_path, file_doc, permission, download_count in values:
        f = FileInfo()
        f.file_id = file_id
        f.file_name = file_name
        f.file_size = file_size
        f.creator = creator
        f.file_path = file_path
        f.file_doc = file_doc
        f.permission = int(permission)
        f.download_count = download_count
        return f


def drop_file_by_id(file_id):
    sql = "delete from `files` where id=%d " % file_id
    global cursor
    cursor.execute(sql)
    connection.commit()
