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
    return render_template('demo.html',params=locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)

