#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --wsgi-file zSPA/wsgi.py --chdir /zSPA/
