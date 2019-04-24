import arrow
from flask import (
    Flask,
    g,
    render_template,
    request,
)
from flask_babel import (
    Babel,
    format_datetime,
    gettext,
    lazy_gettext,
    refresh,
    format_currency,
)

app = Flask(__name__)
babel = Babel(app)

#另外如果你希望在你的应用中使用常量字符串并且在请求之外定义它们的话，你可以使用一个“懒惰”字符串。“懒惰”字符串直到它们实际被使用的时候才会计算。为了使用一个“懒惰”字符串，请使用 lazy_gettext() 函数:
greeting = lazy_gettext('Good afternoon！')

@app.route('/')
def index():
    hello = gettext('Hello World')
    return render_template('index.html', hello=hello)

@app.route('/lazy/')
def greeting():
    return render_template('index.html', hello=greeting)

@app.route('/hello/<name>/')
def hello(name=None):
    paragraph = None
    now = arrow.now()
    time = format_datetime(now, 'EEEE, d. MMMM yyyy H:mm')
    money = format_currency(1000000, 'CNY')
    if name != 'Nobody':
        paragraph = 'Hello %(name)s,\n Now is %(time)s,\nYour house provident fund is %(money)s'
        paragraph = gettext('Hello %(name)s,\n Now is %(time)s,\nYour house provident fund is %(money)s', name=name, time=time, money=money) 
    return render_template('hello.html', paragraph=paragraph)

@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['de', 'fr', 'en', 'zh'])

@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
