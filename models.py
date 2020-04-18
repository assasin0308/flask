from flask import Flask,render_template,\
    request,make_response,redirect
from flask_sqlalchemy import SQLAlchemy
# 防止 ModuleNotFoundError: No module named 'MySQLdb'  报错
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 链接数据库格式 可省略端口号
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:uswepwd@host:port/dbname'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:19920308shibin@127.0.0.1/flask_study"
# SQLALChemy自动追踪程序修改 SQLALCHEMY_TRACK_MODIFICATIONS = true 但会占用内存空间
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# sql执行后自动提交 sb.session.commit()
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 创建SQLALChemy 实例 db
db = SQLAlchemy(app)

# 创建模型
# class MODELNAME(db.MODEL): 定义模型名称 根据表名设定
#     __tablename__ = 'TABLENAME' 数据表名称
#     COLUMN_NAME = db.Column() 映射到数据表列的名称
#     COLUMN_NAME = db.Column(db.TYPE,OPTIONS) db.TYPE:列类型 OPTIONS:列选项

# db.TYPE 类型如下:
#    类型名称            python类型            说明
#   Integer               int                普通整数,32位
#   SmallInteger          int                小范围整数,通常是16位
#   BigInteger            int或long          不限精度整数
#   Float                 float              浮点数
#   Numeric               decimal.Decimal    定点数
#   String                str                变长字符串
#   Text                   str               变长字符串,优化后
#   Unicode                unicode           变长Unicode字符串
#   UnicodeText            unicode           变长Unicode字符串,优化后
#   Boolean                bool              布尔
#   Date                   datetime.date     日期
#   Time                   datetime.time     时间
#   DateTime               datetime.datetime 日期和时间

# OPTIONS 猎德选项说明 多个逗号隔开
#   选项明                     说明
#   primary_key         设置为true表示为主键
#   unique              设置为true表示值唯一
#   index              设置为true表示该类创建索引
#   index              设置为true表示该类创建索引
#   nullable           设置为true表示该类允许为空
#   default            为该列定义默认值

@app.route('/')
def index():
    return 'flask models'

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
# 删除全部表 高危操作!
# db.drop_all()

# 操作数据库 增删该查
#----------insert-------------------------
@app.route('/insert')
def insert_views():
    # 创建 Users 对象
    users = Users('王老师',32,'839203143@qq.com')
    # 将对象通过 db.session.add() 写入
    db.session.add(users)
    # 提交事务
    db.session.commit()
    return 'Insert success'

# 结合表单进行
@app.route('/register',methods=['GET','POST'])
def register_view():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        age = request.form.get('age')
        email = request.form.get('email')
        users = Users(username,age,email)
        db.session.add(users)
        # db.session.commit()
        return 'register success'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)