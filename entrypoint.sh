#!/bin/bash
cd /app

python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn apiAssignment.wsgi:application --bind 0.0.0.0:8000
