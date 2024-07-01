# Django Commands

## Basic Commands

### Create a new site

>`django-admin start project <SITE_NAME> <DIRECTORY>`

Creates a new django project with the below structure

manage.py \
db.file \
<SITE_NAME>/

### Starts Site

>`python3 <SITE_DIRECTORY>/manage.py runserver`


## Migrations

### Adding custom models and running

Create models directory as below within site folder

models/__init__.py
models/model_name.py

Import the models within __init__.py as below

>`from .model_name import ModelName`

Run the below command to create the migrations file.

>`python3 <SITE_DIRECTORY>/manage.py makemigrations <SITE_NAME>`

Then run the migrations

>`python3 <SITE_DIRECTORY>/manage.py migrate`