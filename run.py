from flask import Flask


# 将当前运行得到主程序构建成为Flask的应用,以便接受用户的请求(request)并给出相应(response)
app = Flask(__name__)

# flask中路由定义,定义用户的访问路径
@app.route('/')
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



if __name__ == '__main__':
    app.run(debug=True)  # 启动服务,默认端口 5000

