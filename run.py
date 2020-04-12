from flask import Flask


# 将当前运行得到主程序构建成为Flask的应用,以便接受用户的请求(request)并给出相应(response)
app = Flask(__name__)

# flask中路由定义,定义用户的访问路径
@app.route('/')
def index():
    return "<h1> this is my first app </h1>"

# 带参数的路由
@app.route('/login/<name>') # 参数名称用 <>包裹
def login(name): # 形参与路由参数名称保持一致
    return 'this is login page,name is %s ' %name

@app.route('/register')
def register():
    return "this is register page"


if __name__ == '__main__':
    app.run(debug=True)

