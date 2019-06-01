import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # __name__ : the name of the current Python module.
    # instance_relative_config=True: configuration files are relative to the instance folder. 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from src.libs import sqlite_db
    sqlite_db.init_app(app)

    from src.views.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from src.views.blog import bp as blog_bp
    app.register_blueprint(blog_bp)
    app.add_url_rule('/', endpoint='index')
    return app
