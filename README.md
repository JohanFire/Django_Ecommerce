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

---
## MVT Pattern in Django

Django uses the MVT Pattern = Model > View > Template

---
# Creating Home Page of eCommerce

lets copy the html template and create ecommerce > static folder, then copy the 4 folders inside static
let's do the changes in settings.py and finally execute:

```bash
    python manage.py collectstatic
```

---
# Create "Category" model in Django
1.  `python manage.py startapp category`
2. then we have to register the app in our project, we go to ecommerce > [settings.py](./ecommerce_django/ecommerce/settings.py)
and write in "INSTALLED APPS"
    ```python
        INSTALLED_APPS = [
            ...
            "category",
            ...
        ]
    ```
3. create the Category model in category > [models.py](./ecommerce_django/category/models.py)
   ```python
        # Create your models here.
        class Category(models.Model):
            category_name = models.CharField(max_length=50, unique=True)
            description = models.CharField(max_length=255, blank=False)
            slug = models.CharField(max_length=100, unique=True)
            category_image = models.ImageField(upload="photos/categories", blank=True)

            class Meta: # how will be shown in Django admin panel
                verbose_name= "category" # when singular
                verbose_name_plural = "categories" # when plural

            def __str__(self) -> str:
                return self.category_image + ": " + self.slug
    ```
4. Now to register the new Category entity in Django, have to go to category > [admin.py](./ecommerce_django/category/admin.py)
    ```python
        from .models import Category

        # Register your models here.
        admin.site.register(Category)
    ```

5. Have to install Pillow package so we can upload files like the category_image
    `pip3 install pillow`

6. Now we have to do migrations
`python manage.py makemigrations`
will generete the changes in [0001_initial.py](./ecommerce_django/category/migrations/0001_initial.py) that will do once we migrate:
`python manage.py migrate`
now the table in Django has been generated
---
# Create superuser in Django
`winpty python manage.py createsuperuser`