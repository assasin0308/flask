# Flask

## 1. 介绍

```json
flask是基于python并且依赖于Jinja2模板引擎和WSGI服务的一个微型框架.WSGI(web Server gateway Interface )web服务网关接口.
flask框架模式 - MTV
M: Model,模型层,负责数据库建模
T: Template 模板层,处理与用户显示的内容
V: View,视图层,处理与用户交互的内容
```

## 2. 安装

```python
pip install flask
```

## 3. 快速开始

```python
from flask import Flask

# 将当前运行得到主程序构建成为Flask的应用,以便接受用户的请求(request)并给出相应(response)
app = Flask(__name__)

# flask中路由定义,定义用户的访问路径
@app.route('/')
def index():
    return "<h1> this is my first app </h1>"


if __name__ == '__main__':
    app.run(debug=True) # 启动服务 默认5000端口
```

## 4.

```python

```

## 5.

```python

```

## 6.

```python

```

## 7.

```python

```

## 8.

```

```

## 9.

```

```

## 10.

```

```

## 11.

```json

```

## 12. 

```python

```

## 13. 

```python

```

## 14.

```python

```

## 15.

```python

```

## 16.

```python

```

## 17.

```python

```

## 18.

```

```

## 19.

```

```

## 20.

```

```

## 21.

```json

```

## 22. 

```python

```

## 23. 

```python

```

## 24.

```python

```

## 25.

```python

```

## 26.

```python

```

## 27.

```python

```

## 28.

```

```

## 29.

```

```

## 30.

```

```

