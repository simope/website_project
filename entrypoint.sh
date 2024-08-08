#!/usr/bin/env bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
gunicorn --workers=3 --bind=0.0.0.0:8000 website.wsgi:application