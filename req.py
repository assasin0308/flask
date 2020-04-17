from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'),404


@app.route('/')
def index():
    return 'index method'

# request - 请求对象 封装了所有与请求相关的信息,如请求头
# 请求数据,请求路径
# 在 flask中请求信息封装在了 request 中
# 常用的成员
# scheme: 获取请求方案
# method: 获取本次请求方式
# request.args 获取使用GET请求方式提交的数据
# request.form 获取使用POST请求方式提交的数据
# request.values 获取使用GET/POST请求方式提交的数据
# request.cookies 获取cookie中的信息
# request.headers 获取请求消息头的信息
# request.path  获取访问路径 请求路径
# request.full_path  获取完整的请求路径
# request.url  获取完整的访问地址
# request.files  获取上传文件信息

@app.route('/request')
def request_views():
    # print(request.method)
    # print(dir(request))
    # 请求方案
    scheme = request.scheme   # http
    # 请求方法
    method = request.method  # GET
    # 获取使用GET请求方式提交的数据
    args = request.args
    # 获取使用POST请求方式提交的数据
    form = request.form
    # 获取使用POST请求方式提交的数据
    values = request.values
    # 获取访问路径 请求路径
    path = request.path
    # 获取完整的请求路径
    full_path = request.full_path
    # 获取完整的访问地址
    url = request.url
    # 获取请求消息头的信息 字典
    headers = request.headers
    # 获取请求消息头中的 User-Agent
    user_agent = request.headers['User-Agent']
    # 获取请求消息头中的 referer 请求的原地址;可能不存在
    referer = request.headers.get('referer','')
    # 获取上传文件信息
    files = request.files
    # 获取cookie中的信息
    cookies = request.cookies

    return render_template('request.html',params=locals())

#---------------GET Methos-------------------
@app.route('/form')
def form_views():
    return render_template('form.html')

@app.route('/form_do')
def form_do():
    if request.method == 'GET':
        #获取form表单提交的数据
        uname = request.args.get('uname')
        upwd = request.args.get('upwd')
        print('用户名称: %s,用户密码: %s'%(uname,upwd))

    return '获取表单数据success'

#-----------POST Method-----------------------

@app.route('/post')
def post_form():
    return render_template('post_form.html')

@app.route('/post_form',methods=['POST'])
def post_do():
    if request.method == 'POST':
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        email = request.form.get('email')
        print("用户名:%s,密码:%s,邮件:%s"%(uname,upwd,email))
    else:
        return 'Request Method Not Allowed!'
    return 'POST请求数据获取success'

#-----------update ----------------------------------



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)