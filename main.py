from flask import Flask,render_template,\
    request,make_response,redirect
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)

@app.route('/')
def index():
    return 'flask run success'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

# 部署 pip install gunicore
# gunicore -w 4 -b 127.0.0.1:5000 -D --access-logfile ./logs/log  main:app
# gunicore -w 4 -b 127.0.0.1:5001 -D --access-logfile ./logs/log  main:app
# -w n 开启n个进程 worker
# -b 127.0.0.0:5000 绑定至那个机器
# -D 以后台守护进程方式运行
#  --access-logfile FILE 日志文件存储路径
# main:app  main.py的app对象

# 配置 nginx
# upstram flask {
#     server 127.0.0.1:5000;
#     server 127.0.0.1:5001;
# }
# server {
#     listen      80;
#     server_name  localhost;
#
#     location / {
#         proxy_pass http://flask;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#     }
# }

# nginx -s reload

