# coding: utf-8

from flask import Flask, request

#引入Flask类，Flask类实现了一个WSGI应用
#引入一个文件   采用其中的方法（函数）
import db_helper
import user_service
#引入类
from common_res import CommonRes
from user import User
app = Flask(__name__)
# app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。 
# 让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录。


#使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。 
 #   处理URL和视图函数的关系的程序就是路由，这里的视图函数就是hello_world。 
@app.route('/')
def index():
    return 'Hello World' 
#这个handler可以catch住所有abort(404)以及找不到对应router的处理请求"""
@app.errorhandler(404)
def not_found(error):
    return 'error', 404

#访问URL的方法   浏览器告诉服务器：想在 URL 上 发布 新信息。并且，服务器必须确保 数据已存储且仅存储一次。这是 HTML 表单通常发送数据到服务器的方法。
@app.route('/login', methods=['POST'])
def login():
    """
用户登录  
    :return:
    """
    res = CommonRes()
    #返回给客户端的json格式数据-------------不是很明白
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

#是指url/register只接受POST方法。也可以根据需要修改methods参数
@app.route('/register', methods=['POST'])
def register():
    """
用户注册
    :return:
    """
    u = User()
    user_service.register_user(u)
    return ''

#使用这个判断可以保证当其他文件引用这个文件的时候（例如“from hello import app”）不会执行这个判断内的代码，也就是不会执行app.run函数。
if __name__ == '__main__':
    db_helper.init()
    app.debug = True
    app.secret_key = 'secret_key'
    app.run(host='0.0.0.0')
#执行app.run就可以启动服务了。默认Flask只监听虚拟机的本地127.0.0.1这个地址，端口为5000。 
#   而我们对虚拟机做的端口转发端口是9000，所以需要制定host和port参数，0.0.0.0表示监听所有地址，这样就可以在本机访问了。 
#   服务器启动后，会调用werkzeug.serving.run_simple进入轮询，默认使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求， 
#  实际上还是使用标准库BaseHTTPServer.HTTPServer，通过select.select做0.5秒的“while TRUE”的事件轮询。 
# 当我们访问“http://127.0.0.1:9000/”,通过app.url_map找到注册的“/”这个URL模式,就找到了对应的hello_world函数执行，返回“hello world!”,状态码为200。 
#如果访问一个不存在的路径，如访问“http://127.0.0.1:9000/a”,Flask找不到对应的模式，就会向浏览器返回“Not Found”，状态码为404 