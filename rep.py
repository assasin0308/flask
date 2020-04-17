from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'response ok'
    # return render_template('index.html')

# response 相应对象


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)