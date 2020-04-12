from flask import Flask


# 将当前运行得到主程序构建成为Flask的应用,以便接受用户的请求(request)并给出相应(response)
app = Flask(__name__)

# flask中路由定义,定义用户的访问路径
@app.route('/')
def index():
    return "<h1> this is my first app </h1>"


if __name__ == '__main__':
    app.run(debug=True)

