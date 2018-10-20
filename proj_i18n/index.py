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
    lazy_gettext,
    refresh,
)

app = Flask(__name__)
babel = Babel(app)


@app.route('/hello/<name>')
def hello(name=None):
    now = arrow.now()
    time = format_datetime(now, 'EEEE, d. MMMM yyyy H:mm')
    name = lazy_gettext(name)
    return render_template('hello.html', name=name, time=time)

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
