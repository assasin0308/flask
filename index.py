from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '响应的一句话'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)