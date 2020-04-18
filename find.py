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
# 1. 基于 db.session 进行查询
# 查询函数
    # db.session.query() 返回query对象包含了指定实体类对应的表中所有数据
    # db.session.query(实体或实体的列).all() 列表方式返回查询的所有结果
    # db.session.query(实体或实体的列).first() 列表方式返回查询的第一个结果 没有为None
    # db.session.query(实体或实体的列).first_or_404() 列表方式返回查询的第一个结果 没有则终止并返回404
    # db.session.query(实体或实体的列).count() 列表方式返回查询结果的数量
# 查询过滤器 过滤行 query之后 查询函数之前
    # filter() 按指定条件进行过滤
    # filter_by() 按等值条件进行过滤
    # limit()  限制行数
    # order_by() 根据指定条件进行排序
    # group_by() 根据指定条件进行分组

    # 详解:
    # filter()
    # 查询users数据表年龄大于30的所有数据
    # db.session.query(Users).filter(Users.age>30).all()
    # 查询users数据表id等于5的数据  filter等值必须使用 双等号
    # db.session.query(Users).filter(Users.id == 5).first()
    # db.session.query(Users).filter_by(Users.id = 5).first()
    # like或in模糊查询
    # 查询users数据表email包含'assasin'的所有数据 Users.email.like()
    # db.session.query(Users).filter(Users.email.like('%assasin%')).all()
    # 查询users数据表id在5-8之间的所有数据 Users.email.in_(列表形式查询范围)
    # db.session.query(Users).filter(Users.id.in_([1,2,3])).all()
    # filter_by()
    # 查询users数据表id等于5的数据 只做单表查询 多条件逗号隔开
    # db.session.query(Users).filter_by(id = 5).first()
    # limit()
    # 查询users数据表查询结果中获取前5条
    # db.session.query(Users).limit(5).all()
    # 偏移量查询
    # db.session.query(Users).limit(5).offset(1).all()
    # order_by() 排序函数 排序字段 + 排序规则
    # db.session.query(Users).order_by('id desc').all()
    # group_by() 分组函数
    # db.session.query(Users).group_by('age').all()




@app.route('/query')
def query_views():
    # print(db.session.query(Users,Course))
    # print(db.session.query(Users.username,Users.email))
    # SELECT users.username AS users_username, users.email AS users_email FROM users
    # result = db.session.query(Users).all()
    # for user in result:
    #     print(user.username,user.age,user.email)
    # user = db.session.query(Users).first()
    # print(user.username, user.age, user.email)
    # course = db.session.query(Course).first()
    # print(course)
    # count = db.session.query(Users).count()
    # print(count)

    # 查询过滤器对数据进行筛选
    # 多条件逗号隔开 AND关系
    # users = db.session.query(Users).filter(Users.age > 30,Users.id > 6).all()
    # OR关系 借助 or_() 函数 b.session.query(Users).filter(or_(条件1,条件2)).all()
    # users = db.session.query(Users).filter(or_(Users.age > 25,Users.id > 5)).all()
    # 模糊查询 like
    # users = db.session.query(Users).filter(Users.email.like('%assasin%')).all()
    # 模糊查询 in
    # users = db.session.query(Users).filter(Users.id.in_([5,6,8])).all()
    # filter_by() 查询users数据表id等于5的数据
    # users = db.session.query(Users).filter_by(id = 8).first()
    # 查询users数据表查询结果中获取前5条
    # users = db.session.query(Users).limit(3).all()
    # users = db.session.query(Users).limit(3).offset(1).all()
    # 排序  注意三种写法 由于版本不一致导致
    # users = db.session.query(Users).order_by('id desc').all()  pycharm不支持
    # users = db.session.query(Users).order_by(Users.id.desc()).all()  推荐
    # users = db.session.query(Users).order_by(desc(Users.id)).all()  # 需要导入 desc()函数 from sqlalchemy import desc
    # 二级排序
    # users = db.session.query(Users).order_by(Users.username.asc(),Users.id.desc()).all()
    # 分组
    users = db.session.query(Users).group_by('age').all()
    print(users)
    return 'Query success'
#  2. 或 Models 进行查询

@app.route('/query_all')
def query_all():
    users = db.session.query(Users).all()
    # print(users)
    return render_template('users.html',params = locals())

# --------两种传参方式查询---------------------------
@app.route('/query_by_id/<int:id>')
def query_by_id(id):
    user = db.session.query(Users).filter_by(id = id).first()
    return render_template('user_info.html',params=locals())

@app.route('/query_one')
def query_one():
    id = request.args.get('id')
    user = db.session.query(Users).filter_by(id = id).first()
    return render_template('user_detail.html',params=locals())
# --------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)