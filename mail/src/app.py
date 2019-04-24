# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail

from src.views import blueprint as v1


app = Flask(__name__)
app.config.from_object('src.settings')
app.register_blueprint(v1, url_prefix='/v1')

app.mail = Mail(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

