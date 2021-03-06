# python-flask-pratice

## Flask

Flask 是由 Armin Ronacher 用 Python 編寫的輕量級 Web 應用框架。基於 [Werkzeug](http://werkzeug.palletsprojects.com/en/0.15.x/) 實現的 WSGI 工具箱和 [Jinja2](http://jinja.pocoo.org/docs/2.10/intro/) 模板引擎。設計哲學是只保留核心框架，透過插件等擴充功能。相較於 Django 學習曲線較緩。此倉庫是紀錄學習 flask 的練習代碼。

維護開發 Flask 的團隊 Pallets 的公開練習倉庫：[Flaskr](https://github.com/pallets/flask/tree/master/examples/tutorial)

[Flask 1.0 文檔](http://flask.pocoo.org/docs/1.0/)

## base:
- 練習基本的 flask，並用 Bootstrap 4.1 製作頁面
[Bootstrap 4.1 文檔](https://getbootstrap.com/)
- 練習用 docker 打包
- 參考文檔：https://blog.hasura.io/how-to-write-dockerfiles-for-python-web-apps-6d173842ae1d/

## i18n:
- 練習 flask 插件 Flask-Babel 實現國際化（i18n, internationalization）

### Flask-Babel
- 基於[babel](https://github.com/python-babel/babel)、[pytz](https://pypi.python.org/pypi/pytz/)，支持 i18n 與 L10n的 flask 庫[Flask-Babel](https://github.com/python-babel/babel)

## mail
- 練習用 flask 寄信
- [Flask-Mail 文檔](https://pythonhosted.org/Flask-Mail/)

## blog
- 依照[toturial](http://flask.pocoo.org/docs/1.0/tutorial/#tutorial)建一個簡單的部落格, 數據庫用 sqlite

## markdown\_pagedown
- 依照[Flask-PageDown](https://github.com/miguelgrinberg/Flask-PageDown)練習寫一個 markdown 編輯器
