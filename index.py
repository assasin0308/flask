from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '响应的一句话'

# templates 位置: 默认情况下,flask会在程序文件夹中的 templates 子文件夹中寻找模板


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)