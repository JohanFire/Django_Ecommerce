# Django_Ecommerce

Creating an Ecommerce with Django

# Virtual env

All dependencies and packages for the web, won't affect python's default OS dependencies

## Create virtual env

```bash
    python -m venv .venv
```

## Run virtual env

```bash
    . .venv/Scripts/activate
    # or
    source .venv/Scripts/activate
```

## Exit virtual env

Control + C or

```bash
    deactivate
```

# Django

## Install Django

Of course inside virtual env

```bash
    pip3 install django
```

## Create new Django project

django-admin startproject NAME_APP [actual_directory]

```bash
    django-admin startproject ecommerce .
```

## Run server

```bash
    python manage.py runserver
```

## About Django app generated files by default

init.py
default file that will start in any module

asgi.py & wsgi.py
config to the door of django, it administrate the async door for the server

settings.py
here contains or properties and settings the app need to start

urls.py
contains all urls of the website

## MVT Pattern in Django

Django uses the MVT Pattern = Model > View > Template

# Creating Home Page of eCommerce

lets copy the html template and create ecommerce > static folder, then copy the 4 folders inside static
let's do the changes in settings.py and finally execute:

```bash
    python manage.py collectstatic
```
