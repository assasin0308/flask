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