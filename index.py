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