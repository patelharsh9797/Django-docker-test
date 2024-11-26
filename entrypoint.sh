#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# gunicorn django_test.wsgi:application --bind 0.0.0.0:8000
gunicorn --workers 3 --threads 2 --bind 0.0.0.0:8000 django_test.wsgi:application