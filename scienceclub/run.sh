#!/bin/bash

# pip3 install django
# pip3 install --upgrade djangorestframework-simplejwt

./manage.py makemigrations
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/