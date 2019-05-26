# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template


app = Flask(__name__)
# 從 settings import 變量，slient=True: 找不到不報錯
app.config.from_pyfile('settings', silent=True)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    # 默認 port=5000
    app.run(host='0.0.0.0')
