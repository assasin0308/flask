from flask import Flask,render_template,\
    request,make_response,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 链接数据库格式 可省略端口号
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql//username:uswepwd@host:port/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql//root:19920308shibin@127.0.0.1/flask_study'
# SQLALChemy自动追踪程序修改 SQLALCHEMY_TRACK_MODIFICATIONS = true 但会占用内存空间
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 创建SQLALChemy 实例 db
db = SQLAlchemy(app)







@app.route('/')
def index():
    return 'flask models'

# 创建和使用模型 ORM 特征:
# 对象(表结构映射 + 数据类型映射)
# 关系映射(表之间关系)





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)