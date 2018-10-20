#!/bin/bash

pybabel extract -F babel.cfg -o messages.pot .
pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
pybabel init -i messages.pot -d translations -l zh
pybabel compile -d translations

#run_commands resetTranslation $@
