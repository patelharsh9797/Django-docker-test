#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# gunicorn base.wsgi:application --bind 0.0.0.0:8000
gunicorn --workers 3 --threads 2 --bind 0.0.0.0:8000 base.wsgi:application