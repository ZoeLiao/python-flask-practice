# Flask-Babel
- 基於[babel](https://github.com/python-babel/babel)、[pytz](https://pypi.python.org/pypi/pytz/)，支持 i18n 與 L10n的 flask 庫[Flask-Babel](https://github.com/python-babel/babel)

## i18n
- internationalization，國際化

## L10n ( L 大寫與 i18n 的 i 區別)
- locolization，在地化

## How to use
- `. hello`
- `python index.py`
- 訪問[0.0.0.0:5000/hello/name](0.0.0.0:5000/hello/name)

## 重新編譯
- 可直接 ` . reset`
- 或執行以下指令：
- `pybabel extract -F babel.cfg -o messages.pot .`
- `pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .`
- `pybabel init -i messages.pot -d translations -l zh`
- `pybabel compile -d translations`

## .pot 文件
- Protable Object 的縮寫，是給翻譯人員用的資源文件，可在任何編輯器(vi，Emacs 等)編輯。
- 用 msginit 分析 pot 文件，可產生各語言對應的 po 文件，例如中文就是 zh_TW.po，英文就是 en.po。

## .po 文件
- 與 . pot 文件的性質類似，是從原碼提取需要翻譯的字符串列表。

## mo文件
- Machine Object 的縮寫，為面向機器的，用 msgfmt 將 .po 文件編譯成的二進制文件，無法直接編輯。

