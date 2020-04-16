from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
# 3.4.4



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)