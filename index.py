from flask import Flask, render_template

app = Flask(__name__)

# templates 位置: 默认情况下,flask会在程序文件夹中的 templates 子文件夹中寻找模板
# return render_template() 将模板渲染成字符串并响应给客户端
# render_template('xxx.html',arg1=value1,arg2=value2)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)