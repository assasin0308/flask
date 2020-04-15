from flask import Flask, render_template

app = Flask(__name__)

# 静态文件的处理 所有静态文件都保存在项目文件 static 文件夹中
# 访问静态文件时 通过 /static/...  进行访问
# <img src="/static/....jpg">
#也可反向解析
# url_for('static',filename='<file_path>')
# <img src="{{ url_for('static',filename='images/goods_pic.jpg') }}">


@app.route('/img')
def goods():
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug=True)