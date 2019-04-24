#!/bin/bash

# 第一次
# 解析文件中的 gettext 到 message.pot
pybabel extract -F babel.cfg -o messages.pot .
# 解析文件中的 lazy_gettext 到 message.pot
pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .

# 翻译到指定的语言 - 第一次
pybabel init -i messages.pot -d translations -l zh

# 更新
#pybabel update -i messages.pot -d translations -l zh

# 编译成机器语言
pybabel compile -d translations
