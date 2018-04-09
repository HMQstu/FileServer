# coding: utf-8

from flask import Flask, request, session
import db_helper
import user_service
import file_service
from common_res import CommonRes
from user import User
import json_utils
import permission_manager
import simple_file_info

app = Flask(__name__)


@app.route('/delete', methods=['GET', 'POST'])
def delete_file():
    """
删除文件，传参: id 文件id号 int
    :return:
    """
    res = CommonRes()
    if 'user' not in session:
        res.code = -3
        res.message = 'no user login'
        return json_utils.to_json_res(res)
    user_dict = session['user']
    role = int(user_dict['role'])
    file_id = int(request.values['id'])
    result = file_service.drop_file(file_id, role)
    if result:
        res.code = 0
        res.message = 'success'
    else:
        res.code = -3
        res.message = 'permission denied'
    return json_utils.to_json_res(res)


@app.route('/files', methods=['GET'])
def files():
    res = CommonRes()
    if 'user' not in session:
        res.code = -3
        res.message = 'no user login'
        return json_utils.to_json_res(res)
    user_dict = session['user']
    role = int(user_dict['role'])
    files_list = file_service.visible_files_list(role)
    result = [simple_file_info.parse(x, role) for x in files_list]

    res.code = 0
    res.message = 'success'
    res.data = result
    return json_utils.to_json_res(res)


@app.route('/upload', methods=['POST'])
def upload():
    res = CommonRes()
    if 'user' not in session:
        res.code = -3
        res.message = 'no user login'
        return json_utils.to_json_res(res)
    user_dict = session['user']
    file_io = request.files['file']
    result = file_service.insert_new_file(file_io, user_dict['username'], permission_manager.NORMAL_FILE_PERMISSION)
    if result is not None:
        res.code = 0
        res.message = 'success'
        res.data = result
    else:
        res.code = -1
        res.message = 'error'
    return json_utils.to_json_res(res)


@app.route('/')
def index():
    return session['user']['username']


@app.errorhandler(404)
def not_found(error):
    return 'error', 404


@app.route('/login', methods=['POST'])
def login():
    """
用户登录  
    :return:
    """
    res = CommonRes()
    username = request.form['username']
    password = request.form['password']
    if username is None or password is None:
        res.code = -1
        res.message = 'invalid params'
        return json_utils.to_json_res(res)
    user = user_service.query_user(username, password)
    if user is None:
        res.code = -2
        res.message = 'username or password not correct'
        return json_utils.to_json_res(res)
    session['user'] = user.__dict__
    res.code = 0
    res.message = 'success'
    res.data = user
    return json_utils.to_json_res(res)


@app.route('/register', methods=['POST'])
def register():
    """
用户注册
    :return:
    """
    res = CommonRes()
    username = request.form['username']
    password = request.form['password']
    # role 取值：normal 普通, leader 领导, admin 管理员
    role = request.form['role']
    mail = request.form['mail']
    phone = request.form['phone']

    if username is None or password is None or role is None:
        res.code = -1
        res.message = 'invalid params'
        return json_utils.to_json_res(res)

    u = User()
    u.username = username
    u.password = password
    if 'admin' == role:
        u.role = permission_manager.ROLE_ADMIN
    elif 'leader' == role:
        u.role = permission_manager.ROLE_LEADER
    else:
        u.role = permission_manager.ROLE_NORMAL
    u.mail = mail
    u.phone = phone

    user_service.register_user(u)
    res.code = 0
    res.message = 'success'
    res.data = u
    return json_utils.to_json_res(res)


@app.route('/logout', methods=['GET'])
def logout():
    """
注销用户
    :return:
    """
    res = CommonRes()
    res.code = -3
    res.message = 'no user login'
    if 'user' in session:
        old_user = session['user']
        session.pop('user', None)
        res.code = 0
        res.message = 'success'
        res.data = old_user
    return json_utils.to_json_res(res)


if __name__ == '__main__':
    db_helper.init()
    app.debug = True
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0')
