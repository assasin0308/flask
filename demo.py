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



# 模板包含 多处重复使用的模板代码
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
        'S': 'assasin',
        'WWC': '老王'
     }
    return render_template('demo.html',params=locals(),name='assasin')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)

