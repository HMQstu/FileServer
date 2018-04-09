服务器基地址：http://127.0.0.1:5000

错误码：
0	成功
-1	传递参数错误
-3	登录用户错误
-2	其他错误

role代码：
0   普通用户   normal
4   领导       leader
8   管理员     admin



【登录】
地址：/login
描述：使用用户名、密码进行登录操作
参数：username            用户名         string
      password            密码           string
返回：json字符串 ，如

登录成功：
{
    "message": "success",
    "code": 0,
    "data": {
        "username": "humengqiu",
        "mail": "hmqstu@163.com",
        "password": "242363",
        "role": 0,
        "phone": "18117854900"
    }
}

用户名或密码错误
{
    "message": "username or password not correct",
    "code": -2,
    "data": null
}



【注册】
地址：/register
描述：携带用户信息进行注册操作
参数：username            用户名         string
      password            密码           string
      role                用户角色       string		'admin' or 'leader' or 'normal'
      mail                邮箱           string
      phone               电话           string
返回：json字符串 ，如

注册正确
{
    "message": "success",
    "code": 0,
    "data": {
        "username": "humengqiu",
        "mail": "hmqstu@163.com",
        "password": "242363",
        "role": 0,
        "phone": "18117854900"
    }
}

注册出错
{
    "message": "invalid params",
    "code": -1,
    "data": null
}



【退出系统】
地址：/loguot
描述：注销当前登录用户的操作
参数：无
     返回：json字符串 ，如

用户未登录时
{
    "message": "no user login",
    "code": -3,
    "data": null
}

成功退出
{
    "message": "success",
    "code": 0,
    "data": {
        "username": "humengqiu",
        "mail": "hmqstu@163.com",
        "password": "242363",
        "role": 0,
        "phone": "18117854900"
    }
}



【文件上传】
地址：/upload
描述：上传文件的操作
参数：file                文件         file
返回：json字符串 ，如

上传出错
{
    "message": "error",
    "code": -1,
    "data": null
}

上传正确
{
    "message": "success",
    "code": 0,
    "data": {
        "creator": "humengqiu",
        "file_name": "计算机操作系统(汤子瀛)习题答案.DOC.pdf",
        "created_at": 1523263233667,
        "permission": 1503,
        "file_path": "F:\\humengqiu\\workpace\\FileServer\\计算机操作系统(汤子瀛)习题答案.DOC.pdf",
        "file_id": 0,
        "file_size": 105154,
        "download_count": 0,
        "file_doc": "pdf"
    }
}



【删除文件】
地址：/delete
描述：删除单条文件记录的操作
参数：id                文件id号         int
返回：json字符串 ，如

用户未登录
{
    "message": "no user login",
    "code": -3,
    "data": null
}

成功删除
{
    "message": "success",
    "code": 0,
    "data": null
}

所删文件不存在
{
    "message": "no such file",
    "code": -1,
    "data": null
}

没有操作权限
{
    "message": "permission denied",
    "code": -3,
    "data": null
}



【文件列表 】
地址：/files
描述：获取全部文件列表的操作
参数：无
返回：json字符串 ，如

{
    "message": "success",
    "code": 0,
    "data": [
        {
            "creator": "humengqiu",
            "file_name": "计算机操作系统(汤子瀛)习题答案.DOC.pdf",
            "created_at": 1523263233667,
            "can_download": true,
            "file_id": 1,
            "can_delete": false,
            "file_size": 105154,
            "can_see": true,
            "download_count": 0,
            "file_doc": "pdf"
        },
        {
            "creator": "humengqiu",
            "file_name": "本科论文英文扉页模板.doc",
            "created_at": 1523272553823,
            "can_download": true,
            "file_id": 2,
            "can_delete": false,
            "file_size": 153600,
            "can_see": true,
            "download_count": 0,
            "file_doc": "doc"
        },
        {
            "creator": "humengqiu",
            "file_name": "本科毕业论文摘要模板.doc",
            "created_at": 1523272567023,
            "can_download": true,
            "file_id": 3,
            "can_delete": false,
            "file_size": 35328,
            "can_see": true,
            "download_count": 0,
            "file_doc": "doc"
        },
        {
            "creator": "lisi",
            "file_name": "本科毕业设计（论文）封面模版.doc",
            "created_at": 1523272705382,
            "can_download": true,
            "file_id": 4,
            "can_delete": false,
            "file_size": 807424,
            "can_see": true,
            "download_count": 0,
            "file_doc": "doc"
        },
        {
            "creator": "lisi",
            "file_name": "本科毕业设计（翻译）封面模板.doc",
            "created_at": 1523272718589,
            "can_download": true,
            "file_id": 5,
            "can_delete": false,
            "file_size": 5223424,
            "can_see": true,
            "download_count": 0,
            "file_doc": "doc"
        }
    ]
}


