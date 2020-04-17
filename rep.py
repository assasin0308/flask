from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect

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
        file_info = request.files.get('uimg')
        # file_info = request.files['uimg']
        print(file_info)
        return 'ok'

    # 3-10-9 28:00



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)