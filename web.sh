#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate
exec gunicorn mysite.wsgi --bind 0.0.0.0:8000