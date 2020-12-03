# New Book Builder Project

Steps to create a new app from scratch

### Setup the environment

    python3 -m venv .venv
    
    source .venv/bin/activate
    
    pip freeze  # Includes Django
    
    which python

### Create a blank Django project

    django-admin startproject bookbuilder
    
    tree bookbuilder
    
    bookbuilder
    ├── bookbuilder
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
    
### Test the blank project

    cd bookbuilder
    
    python manage.py migrate
    
    python manage.py runserver
    
    Browse http://127.0.0.1:8000/
 
### Add "book" app

    python manage.py startapp book
    
    tree 
    
    .
    ├── book
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── bookbuilder
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    └── manage.py

Create HTML templates

    mkdir templates
    
Edit app2/settings.py  to load the templates

    TEMPLATES = [
        {
            ...
            'DIRS': ['templates'],
            ...
        },
    ]

Create templates/index.html

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>Book Builder</title>
    </head>

    <body>
        <h1>Book Builder</h1>
    </body>

    </html>

Edit bookbuilder/urls.py
    
    from django.views.generic import TemplateView
    from django.urls import path


    urlpatterns = [
        path('', TemplateView.as_view(template_name='index.html')),
    ]

Test the application

    python manage.py runserver
    
    browse to http://127.0.0.1:8000/
    

