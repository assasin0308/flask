from flask import Flask, render_template


# template_folder 配置自定义模板文件目录
# static_url_path 配置自定义静态文件访问路径
# static_folder 配置自定义静态文件目录
app = Flask(
            __name__,
            template_folder='muban',
            static_url_path='/sta',
            static_folder='sta'
            )

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)