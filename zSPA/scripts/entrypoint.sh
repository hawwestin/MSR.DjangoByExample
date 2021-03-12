#!/bin/sh

set -e

echo $MIGRATE
echo "DEBUG " $DEBUG

# if some debug true make migrations
if $MIGRATE  ; then
    python manage.py makemigrations
    python manage.py migrate
fi
# create super user.

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --wsgi-file zSPA/wsgi.py --chdir /zSPA/
