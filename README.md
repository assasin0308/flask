# Flask

## 1. introduce

```json
flask是基于python并且依赖于Jinja2模板引擎和WSGI服务的一个微型框架.WSGI(web Server gateway Interface )web服务网关接口.
flask框架模式 - MTV
M: Model,模型层,负责数据库建模
T: Template 模板层,处理与用户显示的内容
V: View,视图层,处理与用户交互的内容
```

## 2. installation

```python
pip install flask
```

## 3. soso start

```python
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

# template 模板




if __name__ == '__main__':
    app.run(debug=True)  # 启动服务,默认端口 5000


```

## 4. templates & variables

```python
from flask import Flask, render_template

app = Flask(__name__)

# templates 位置: 默认情况下,flask会在程序文件夹中的 templates 子文件夹中寻找模板
# return render_template() 将模板渲染成字符串并响应给客户端
# render_template('xxx.html',arg1=value1,arg2=value2)
@app.route('/')
def index():
    return render_template('index.html')

# templates 模板中的语法
# 变量是一种特殊的占位符,在模板中: {{ 变量名 }}
@app.route('/user')
def user_list():
    return render_template('index.html',name='assasin',age=52)

# templates 传递 字典 & 列表 & 元祖
@app.route('/book')
def book_info():
    # book_info = {
    #     'title':'书籍信息',
    #     'book_name':'钢铁是咋连城的',
    #     'author':'奥斯特洛夫斯基',
    #     'price':32.5,
    #     'publisher':'北京大学出版社'
    # }
    # return render_template('index.html',book_info=book_info)
    title = '书籍信息'
    book_name = '钢铁是咋练成的'
    author = '奥斯特洛夫斯基'
    price = 32.5
    publisher = '北京大学出版社'
    # locals() 函数 将当前所在作用于中的局部变量封装为一个字典,
    # 字典中的键是变量的值,值就是变量的值
    list = [
        '金毛狮王',
        '青翼蝠王',
        '紫衫龙王',
        '白眉鹰王',
    ]
    tup = ('黎明','张学友','刘德华','郭富城')
    dic = {
        'W':'老魏',
        'S':'史斌',
        'WWC':'老王'
    }
    per = Person()
    per.name = '漩涡鸣人' # 对象属性

    # 过滤器 允许在变量输出之前改变变量的值
    # 语法 {{变量|过滤器}}
    # Jinjia2 支持的变量过滤器
    # capitalize   首字符变大写,其他小写(英文)
    # lower        将值转为小写再输出
    # upper        将值转为大写再输出
    # title       将值中的每个单词的首字母变大写
    # trim        将值两端的空格去掉
    uname = 'uzumaki naruto'
    return render_template('index.html',book_info=locals())

class Person(object):
    name = None
    def say(self):
        return "hello i'm a person"



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
```

```html
# templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{book_info.title}}</title>
    <style>
        .container{
            width: 90%;
            margin: 0 auto;
            color: blue;
        }
        .container .title{
            color: aqua;
            background-color: antiquewhite;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="title">{{book_info.title}}</div>
    <div>
        <h3>name is: {{name}}</h3>
        <h3>age is: {{age}}</h3>
    </div>
    <h3>书名:{{book_info.book_name}}</h3>
    <h3>作者:{{book_info.author}}</h3>
    <h3>价格:{{book_info.price}}</h3>
    <h3>出版社:{{book_info.publisher}}</h3>
    <!--获取列表中第二个元素-->
    <h3>list[1]:  {{book_info.list[1]}}  或者   {{book_info.list.1}}</h3>
    <!--获取元组中第三个元素-->
    <h3>tup[2]: {{book_info.tup[2]}}  或者 {{book_info.tup.2}}</h3>
    <!--获取字典中键是WWc的值-->
    <h3>dic['WWC']:   {{book_info.dic.WWC}}</h3>
    <!--获取 per 对象的name属性值-->
    <h3>per.name:   {{book_info.per.name}}</h3>
    <!--调用 per 对象的say方法-->
    <h3>per_say():   {{book_info.per.say()}} </h3>
</div>
</body>
</html>
```

## 5. tempaltes & filter

```html
# 过滤器 允许在变量输出之前改变变量的值
# 语法 {{变量|过滤器}}
# Jinjia2 支持的变量过滤器
# capitalize   首字符变大写,其他小写(英文)
# lower        将值转为小写再输出
# upper        将值转为大写再输出
# title       将值中的每个单词的首字母变大写
# trim        将值两端的空格去掉

<!--过滤器-->
<h3>{{book_info.uname}}</h3>
<h3>capitalize: {{book_info.uname|capitalize}}</h3>
<h3>upper: {{book_info.uname|upper}}</h3>
<h3>title: {{book_info.uname|title}}</h3>
```

## 6. templates & if & for

```python
#demo.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return '首页登录'
# 控制结构
# 语法:
# {% if 条件 %}
# {% endif %}

# {% if 条件 %}
# 满足执行
# {% else %}
# 不满足执行
# {% endif %}
@app.route('/user_list')
def user_list():
    # uname = 'uzumaki naruto'
    return render_template('demo.html',params=locals())

# for循环
# {% for 变量 in tuple|list|dic %}
# {% endfor %}


# 宏 {% macro %} 标签申明宏
# {% macro show(str) %}
#  <h1>{{ str }}</h1>
# ......宏的内容
# {% endmacro %}

#...... 以上是声明,下边是调用
# {{ show(uname) }}
# 为方便重复使用,可将宏放在单独的模板文件
# 1.创建 macro.html 模板文件
# 2.在使用的网页中导入 macro.html
# {% import  'macro.html' as macros %}
#  {{ macros.show(name)}}



# 模板包含 多处重复使用的模板代码,被包含的模板也可以使用直接使用父级模板变量
# {% include 'xxx.html' %}

@app.route('/books')
def book_list():
    list = [
        '金毛狮王',
        '青翼蝠王',
        '紫衫龙王',
        '白眉鹰王',
    ]
    tup = ('黎明', '张学友', '刘德华', '郭富城')
    dic = {
        'W': '老魏',
        'S': '史斌',
        'WWC': '老王'
     }
    return render_template('demo.html',params=locals(),name='assasin')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)



```

```html
# demo.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>控制结构</title>
</head>
<body>
<!--if-endif-->
{% if params.uname %}
<h1>欢迎:{{ params.uname }}</h1>
{% endif %}

<!--if-else-endif-->
{% if params.uname %}
<h1>欢迎:{{ params.uname }}</h1>
{% else %}
<a href="{{ url_for('login')}} ">登录首页去</a>
{% endif %}

<!--for-->
<div style="font-size: 20px">
    {% for str in params.list %}
    <p>{{ str }}</p>
    {% endfor %}
</div>
<ul>
    {% for str in params.tup %}
    <li>{{str}}</li>
    {% endfor %}
</ul>

<div style="color: blue;">
   {% for key,value  in params.dic.items() %}
    <p>{{key}} : {{value}}</p>
    {% endfor %}
</div>

<!--声明一个宏-->
{% macro show(name) %}
<li style="color: blueviolet">{{name}}</li>
{% endmacro %}
<h2>使用宏显示数据</h2>
<ul>
    {% for name in params.list %}
    {{ show(name) }}
    {% endfor %}
</ul>


<h2>引入宏文件</h2>
{% import 'macro.html' as macros %}
<ul>
    {% for str in params.tup %}
    {{ macros.show_li(str) }}
    {% endfor %}
</ul>


<!--包含模板文件-->
{% include 'head.html' %}

<div>自己的</div>
</body>
</html>
```

```html
# macro.html
{% macro show_li(str) %}
    <li>
        <p style="font-size: 18px;">内容</p>
        <span style="color: aqua"> {{ str }} </span>
    </li>
{% endmacro%}
```

```html
# head.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>head</title>
</head>
<body>
    <div class="container">
        <div class="top">
            <h2>网页头部</h2>
        </div>
        <div class="nav">
            <ul>
                <li>
                    <a href="#">导航一</a>
                </li>
                <li>
                    <a href="#">导航二</a>
                </li>
                <li>
                    <a href="#">导航三</a>
                </li>
                <li>
                    <a href="#">{{name}}</a>
                </li>
            </ul>
        </div>
    </div>
</body>
</html>
```

## 7. templates static & block & extends

```python
from flask import Flask, render_template

app = Flask(__name__)

# 静态文件的处理 所有静态文件都保存在项目文件 static 文件夹中
# 访问静态文件时 通过 /static/...  进行访问
# <img src="/static/....jpg">
#也可反向解析
# url_for('static',filename='<file_path>')
# <img src="{{ url_for('static',filename='images/goods_pic.jpg') }}">

# 模板的继承 类似于类的继承
# 语法:
# 1. 父模板中 定义出哪些内容在子模板中是可以被继承/重写的
# {% block  块名 %}
# ......
# {% endblock %}
# 2. 在子模板中 体现继承关系: {% extends '父模板名称' %}
# 在子模板中 要重写的话 :
# {% block 块名 %} .....这里会覆盖父模板内容 {% endblock %}
# 来重写覆盖父模板中内容

# 可通过 {{ super() }} 函数调用父模板中的内容

@app.route('/parent')
def index():
    return render_template('parent.html')

@app.route('/child')
def index_child():
    return render_template('child.html')

@app.route('/img')
def goods():
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug=True)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>static处理</title>
    <!--<link rel="stylesheet" href="/static/css/temp.css">-->
    <link rel="stylesheet" href="{{url_for('static',filename='css/temp.css')}}">
</head>
<body>
<div>
    <!--<img src="/static/images/goods_pic.jpg" alt="my girl friend"  class="img">-->
    <img src="{{url_for('static',filename='images/goods_pic.jpg')}}" alt="my girl friend"  class="img">
</div>
</body>
</html>
```

```html
# parent.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>parent templates</title>
</head>
<body>
<h1>这是父模板 头部内容</h1>
{% block container %}
<h1>这是父模板 主题内容</h1>
{% endblock %}
<h1>这是父模板 底部内容</h1>


</body>
</html>
```

```html
# child.html
{% extends  'parent.html' %}
<!--重写 parent.html 中的container内容-->
{% block container %}
<!--调用父模板内容-->
{{ super() }}
<h1 style="color: red">这是子模板中重写的内容</h1>
{% endblock%}
```

## 8. 404 page

```python
#  自定义404错误页面 @app.errorhandler(404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404 # 返回状态码 否则就会200

@app.errorhandler(500)
def inter_err(e):
    return render_template('500.html'),500
```

## 9. edit configuration

```python
from flask import Flask, render_template


# template_folder 配置自定义模板文件目录
# static_url_path 配置自定义静态文件访问路径
# static_folder 配置自定义静态文件目录
app = Flask(
            __name__,
            template_folder='muban',
            static_url_path='/sta',
            static_folder='sta'
            )

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)
```

## 10. request 

```python
# from flask import request

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

# @app.route('/post')
# def post_form():
#     return render_template('post_form.html')
#
# @app.route('/post_form',methods=['POST'])
# def post_do():
#     if request.method == 'POST':
#         uname = request.form.get('uname')
#         upwd = request.form.get('upwd')
#         email = request.form.get('email')
#         print("用户名:%s,密码:%s,邮件:%s"%(uname,upwd,email))
#     else:
#         return 'Request Method Not Allowed!'
#     return 'POST请求数据获取success'

#-----------update ----------------------------------
# POST GET 合二为一
@app.route('/post',methods=['GET','POST'])
def post_form():
    if request.method == 'GET':
        # 展示表单
        return render_template('post_form.html')
    elif request.method == 'POST':
        # 处理表单数据
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        email = request.form.get('email')
        print("用户名:%s,密码:%s,邮件:%s" % (uname, upwd, email))

    return 'POST请求数据获取success'




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)
```

## 11. response & upload file

```python
# from flask import make_response

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
import time


app = Flask(__name__)


@app.route('/')
def index():
    return 'response ok'
    # return render_template('index.html')

# response 相应对象 make_response() 构建相应对象
# resp = make_response('响应内容')
# return resp

@app.route('/response')
def response_views():
    # 使用响应对象响应内容
    # resp = make_response('使用响应对象响应内容')
    # 创建相应对象,并赋值响应模板
    res = {
        "name":"assasin",
        "age":52
    }
    # resp = make_response(render_template('post_form.html'))
    resp = make_response({"errcode":0,"errmsg":'success',"result":res})
    # 返回响应内容
    return resp
    # 重定向到 index.html
    # return redirect('index.html')


# 重定向 redirect
# from flask import redirect
# return redirect('/')
@app.route('/view')
def redirect_vews():
    # 重定向至上边的路径
    return redirect('response')

# -------------------文件上传-------------
@app.route('/file',methods=['GET','POST'])
def file_view():
    if request.method == 'GET':
        return render_template('file_upload.html')
    else:
        # 服务器端接收上传文件
        file = request.files.get('uimg')
        # file_info = request.files['uimg']
        # file.filename 获取文件名称
        filename = file.filename;
        # file.save(保存路径) 将文件保存至指定目录
        # file.save('static/uploads/' + filename)
        # # 修改文件名称 并修改文件名
        file.save('static/uploads/' + 'assasin.png')
        # print(filename)
        return 'uploads ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)
```

## 12. 

```python

```

## 13. 

```python

```

## 14.

```python

```

## 15.

```python

```

## 16.

```python

```

## 17.

```python

```

## 18.

```python

```

## 19.

```python

```

## 20.

```python

```

## 21.

```python

```

## 22. 

```python

```

## 23. 

```python

```

## 24.

```python

```

## 25.

```python

```

## 26.

```python

```

## 27.

```python

```

## 28.

```python

```

## 29.

```python

```

## 30.

```python

```

## 31.

```python

```

## 32. 

```python

```

## 33. 

```python

```

## 34.

```python

```

## 35.

```python

```

## 36.

```python

```

## 37.

```python

```

## 38.

```python

```

## 39.

```python

```

## 40.

```python

```

