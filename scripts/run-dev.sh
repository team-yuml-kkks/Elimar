#!/bin/sh

pip install -r requirements/local.txt

python manage.py migrate
python manage.py loaddata elimar/modules/users/fixtures/users_accounts.json
python manage.py runserver 0.0.0.0:8000
