# coding: utf-8

from flask import Flask, request
import db_helper
import user_service
import file_service
from common_res import CommonRes
from user import User
import json_utils

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    file_io = request.files['file']
    result = file_service.insert_new_file(file_io, None, None)
    res = CommonRes()
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
    return 'Hello World'


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
    u = User()
    user_service.register_user(u)
    return ''


if __name__ == '__main__':
    db_helper.init()
    app.debug = True
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0')
