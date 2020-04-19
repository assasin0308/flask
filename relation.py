from flask import Flask,render_template,request,make_response,redirect
from flask_sqlalchemy import SQLAlchemy
# 查询 Or 关系
from sqlalchemy import or_, desc

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
    # 一门课程可以由多名老师教授  一对多

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

# 关系映射 teacher-->course
# 每名老师教一门课程  一对一
# 一门课程可以由多名老师教授  一对多
# 语法实现:
# 1. 外键列明 = db.Column(db.Integer,db.ForeignKey('主表.主键'))
# 2. 属性名称 = db.relationship('多的实体类名',backref='属性名')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)