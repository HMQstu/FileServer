# coding: utf-8

from flask import Flask, request

import db_helper
import user_service
from common_res import CommonRes
from user import User

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


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
        return res.to_res()
    user = user_service.query_user(username, password)
    if user is None:
        res.code = -2
        res.message = 'username or password not correct'
        return res.to_res()
    # user 不为 None，即登录成功
    res.code = 0
    res.message = 'success'
    res.data = user
    return res.to_res()


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
