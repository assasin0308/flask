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

# course:teacher => 1:n

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer)
    # 一门课程可以由多名老师教授  一对多 增加一列 course_id
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))

    # 一名老师 只有一个 wife
    # 增加反向引用, Teacher 中得到一个 Wife的信息,同时在Wife中也能得到一个Teacher的信息
    wife = db.relationship('Wife',backref='teacher',uselist=False)
    # uselist=False 查询出的是一个对象,而不是列表


    def __init__(self, tname, tage):
        self.tname = tname
        self.tage = tage

    def __repr__(self):
        return '<Teacher:%r>' % self.tname

#
class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    wage = db.Column(db.Integer)
    # 增加一列 表示引用自 teacher表的主键
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))

    def __init__(self,wname,wage):
        self.wname = wname
        self.wage = wage

    def __repr__(self):
        return "<Wife %r>" % self.wname


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    # 反向引用 返回与当前课程相关的teacher列表
    # backref:定义反向关系 会向teacher是体重增加一个course属性,
    # 可替代course_id来访问Course模型,此时获得到的是模型对象,而不是外键值
    teachers = db.relationship('Teacher',backref='course',lazy='dynamic')

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return '<Course:%r>' % self.cname


# 将创建好的实体类映射回数据库
# db.drop_all()
db.create_all()

# 关系映射 teacher-->course
# 每名老师教一门课程  一对一
# 一门课程可以由多名老师教授  一对多
# 语法实现:
# 1. 外键列明 = db.Column(db.Integer,db.ForeignKey('主表.主键'))
# 2. 属性名称 = db.relationship('多的实体类名',backref='属性名',lazy='dynamic')
    # backref:在关系的另一个模型中添加反向引用

    # lazy : lazy=select:首次访问时加载
    # lazy : lazy=immediate:原对象加载后立即加载关联数据
    # lazy : lazy=subquery: 立即加载,但使用子查询方式
    # lazy : lazy=noload: 永不加载
    # lazy : lazy=dynamic: 动态加载,不加载记录,但提供加载记录的查询

    # uselist 若设置为False,则不使用列表,使用标量

    # secondary 指定多对多关系中关联表的名称


@app.route('/add_course')
def add_course():
    course1 = Course('python基础')
    course2 = Course('python高级')
    course3 = Course('python web基础')
    course4 = Course('python web高级')

    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    return 'Add course success'

@app.route('/add_teacher')
def add_teacher():
    teacher = Teacher('魏老师',35)
    # teacher.course_id = 1
    # 根据course_id查询Course实体,将Course实体赋值给teacher
    course = Course.query.filter_by(id = 1).first()
    teacher.course = course
    # print(course)
    db.session.add(teacher)

    return 'Add teacher success'

@app.route('/register_teacher',methods=['GET','POST'])
def register_teacher():
    if request.method == 'GET':
        courses = Course.query.all()
        return render_template('register_teacher.html',params = locals())
    else:
        tname = request.form.get('tname')
        tage = request.form.get('tage')
        course_id = request.form.get('course_id')
        course = Course.query.filter_by(id = course_id).first()
        # 创建teacher对象,并将course对象赋值给teacher对象
        teacher = Teacher(tname,tage)
        teacher.course = course
        # 保存teacher对象
        db.session.add(teacher)

        # return 'register teacher success'
        return redirect('/show_teacher')

@app.route('/query_teacher')
def query_teacher():
    # 通过 course 对象查询对应所有的 teacher
    course = Course.query.filter_by(id = 1).first()
    # 根据 course 对象查询所有的 teacher 对象
    # teacher = course.teachers.all()
    # 通过 teacher 查询 course
    teacher = Teacher.query.filter_by(tname='吕老师').first()
    # teacher.course
    print(teacher.course)
    return 'Query success'

@app.route('/show_teacher')
def show_teacher():
    teachers = Teacher.query.all()
    return render_template('show_teachers.html',params = locals())

@app.route('/query_teacher_course')
def query_teacher_course():
    # 手动连接查询
    results = db.session.query(Teacher,Course).\
        filter(Teacher.course_id == Course.id).all()
    # print(results)
    for result in results:
        # print(dir(result))
        print('老师:%s;课程:%s'%(result.Teacher.tname,result.Course.cname))
    return 'Query success'

@app.route('/add_wife')
def add_wife():
    # 查询信息
    teacher = Teacher.query.filter_by(id = 2).first()
    # 创建对象
    wife = Wife('王夫人',25)
    # 赋值
    wife.teacher = teacher
    #保存
    db.session.add(wife)
    return 'Add wife success'

@app.route('/query_wife')
def query_wife():
    # 通过 teacher 查询 wife
    teacher = Teacher.query.filter_by(tname='王老师').first()
    wife = teacher.wife
    print("%s的媳妇是%s" %(teacher.tname,wife.wname))
    # 通过 wife 查询 teacher
    wife = Wife.query.filter_by(wname='王夫人').first()
    teacher = wife.teacher
    print('%s的官人是%s' %(wife.wname,teacher.tname))
    return 'Query wife success'

@app.route('/register_wife',methods=['GET','POST'])
def register_wife():
    if request.method == 'GET':
        teachers = Teacher.query.all()
        return render_template('register_wife.html',params = locals())
    else:
        teacher_id = request.form.get('teacher')
        wife = Wife.query.filter_by(teacher_id = teacher_id).first()
        if wife :
            errmsg = 'exist'
            teachers = Teacher.query.all()
            return render_template('register_wife.html', params=locals())
        else:
            wname = request.form.get('wname')
            wage = request.form.get('wage')
            teacher = Teacher.query.filter_by(id = teacher_id).first()
            wife = Wife(wname,wage)
            wife.teacher = teacher
            db.session.add(wife)
        # print(teacher_id)

        return 'register wife success'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)