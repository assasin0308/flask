from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
import time,datetime
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'response ok'
    # return render_template('index.html')

# response 相应对象 make_response() 构建相应对象
# resp = make_response('响应内容')
# return resp

@app.route('/response')
def response_views():
    # 使用响应对象响应内容
    # resp = make_response('使用响应对象响应内容')
    # 创建相应对象,并赋值响应模板
    res = {
        "name":"assasin",
        "age":52
    }
    # resp = make_response(render_template('post_form.html'))
    resp = make_response({"errcode":0,"errmsg":'success',"result":res})
    # 返回响应内容
    return resp
    # 重定向到 index.html
    # return redirect('index.html')


# 重定向 redirect
# from flask import redirect
# return redirect('/')
@app.route('/view')
def redirect_vews():
    # 重定向至上边的路径
    return redirect('response')

# -------------------文件上传-------------
@app.route('/file',methods=['GET','POST'])
def file_view():
    if request.method == 'GET':
        return render_template('file_upload.html')
    else:
        # 服务器端接收上传文件
        file = request.files.get('uimg')
        # file_info = request.files['uimg']
        # file.filename 获取文件名称
        filename = file.filename
        # file.save(保存路径) 将文件保存至指定目录
        # file.save('static/uploads/' + filename)
        #  修改文件名称 并修改文件名
        # 获取后缀
        ext = file.filename.split('.')[1]
        # file.save('static/uploads/' + 'assasin.png')
        # ftime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        filename = ftime  + '.' + ext
        # 绝对路径
        base_dir = os.path.dirname(__file__)
        upload_path = os.path.join(base_dir,'static/uploads/',filename)
        file.save(upload_path)
        print(filename)
        return 'uploads ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)