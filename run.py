from flask import Flask, url_for

# 将当前运行得到主程序构建成为Flask的应用,以便接受用户的请求(request)并给出相应(response)
app = Flask(__name__)

# flask中路由定义,定义用户的访问路径
@app.route('/index')
def index():
    return "<h1> this is my first app </h1>"

# 带一个参数的路由
@app.route('/login/<name>') # 参数名称用 <>包裹
def login(name): # 形参与路由参数名称保持一致
    return 'this is login page,name is %s ' %name

# 带两个参数的访问
@app.route('/register/<name>/<age>')
def register(name,age):
    return "this is register page,name is %s,age is %d."%(name, int(age))

# 指定参数类型的路由定义 如: <int:age> 参数age是一个整形
@app.route('/show/<name>/<int:age>')
def show(name,age):
    age += 1 # age 是 int,直接运算
    return "this is register page,name is %s,age is %d."%(name, age)

# 多 URL 的路由匹配,允许在一个视图处理函数中设置多个url路由规则
@app.route('/')
@app.route('/index_page')
@app.route('/<int:page>')
def index_page(page=None):
    if page is None:
        page = 1
    return "<h1> 这是首页 ......,page is %d </h1>" %page

# 路由中设置HTTP请求方法  POST
@app.route('/user_list',methods=['POST']) #  ['GET','POST']
def user_list():
    return 'this is post request method'

# URL的反向解析:通过视图处理函数的名称自动生成视图处理函数的访问路径
# url_for() 用于反向解析URL
# 第一个参数: 指向函数名称(通过@app.route()修饰的函数)
# 后续参数,对应要构建的url上的变量

@app.route('/url')
def url_views():
    # 将 url_views 反向解析访问地址
    return url_for('index_page') # /index_page

@app.route('/url2')
def url_show():
    return url_for('show',name='shibin',age=52) # /show/shibin/52

# url_for('static',filename='style.css') # 用于静态文件反向解析


if __name__ == '__main__':
    app.run(debug=True)  # 启动服务,默认端口 5000

