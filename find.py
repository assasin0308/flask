from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:19920308shibin@127.0.0.1/flask_study"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 创建 Users类,映射 users表
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True) # 主键 + 整数 = 自增
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return '<Users:%r>'% self.username

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)

    def __init__(self,sname,sage):
        self.sname = sname
        self.sage = sage

    def __repr__(self):
        return '<Student:%r>'% self.sname

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer)

    def __init__(self, tname, tage):
        self.tname = tname
        self.tage = tage

    def __repr__(self):
        return '<Teacher:%r>' % self.tname


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return '<Course:%r>' % self.cname


# 将创建好的实体类映射回数据库
db.create_all()

#----------insert-------------------------
@app.route('/insert')
def insert_views():
    # 创建 Users 对象
    users = Users('石老师',32,'839203145@qq.com')
    # 将对象通过 db.session.add() 写入
    db.session.add(users)
    # 提交事务
    db.session.commit()
    return 'Insert success'

#-------------------select---------------------
# 1. 基于 db.session 进行查询  db.session.query() 返回query对象包含了指定实体类对应的表中所有数据
@app.route('/query')
def query_views():
    print(db.session.query(Users.username,Users.email))
    # SELECT users.username AS users_username, users.email AS users_email FROM users
    return 'query success'
#  2. 或 Models 进行查询






if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)