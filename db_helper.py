# coding: utf-8
from user import User
import mysql.connector


# 注释：数据库操作

connection = None

def init():
    global connection
    connection = mysql.connector.connect(user='root', password='root', database='file_server_db', use_unicode=True)
    return


def check_create():
    sql = '''
        create table if not exists user(
            id bigint primary key auto_increment,
            username varchar(255),
            password varchar(255),
            role int,
            mail varchar(40),
            phone varchar(15)
        );
    '''
    pass


def dispose():
    pass


def find_user_by_username(username):
    # SQL语句
    sql = 'select username,password,role,mail,phone from user where username=%s' % username
    # 执行SQL
    # 填充User
    u = User()
    # 返回User
    return None


def insert_user(user):
    # 执行插入语句
    sql = "insert into user(id,username,password,role,mail,phone) values(0,'%s','%s',%d,'%s','%s')" \
            % user.username, user.password,user.role,user.mail,user.phone
    pass


def remove_user_by_username(username):
    # 执行删除语句
    sql = 'delete from user where username = %s' % username
    pass
