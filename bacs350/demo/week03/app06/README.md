# Demo 6 - Template View

Application notes for learning about Web Hosting


## Steps to build demo code

Follow each of these steps carefully to produce the results that are
are required by this project.  

This project will require you to setup the development tools for local
editing on your computer system.

Follow each step until it is complete.  Do not continue on unless it
is correct.


### Step 1 - Start a Django Project

Begin Project 2 when you have fully completed Project 1

Activate your virtual environment

Mac - Activate Virtual Environment

    source ./.venv/bin/activate
    
Windows - Activate Virtual Environment

    .venv/Scripts/activate.bat

Check your VENV

    pip freeze
    
    deactivate  (when you are all done)

Start project02
    
    django-admin startproject project02
    
    python manage.py migrate 
    
    python manage.py runserver
    
Browse to http://localhost:8000

You should get the Django test page


### Step 2 - Start a Django App

    python manage.py startapp notes
    
project02/urls.py

    urlpatterns = [
        path('', IndexPage.as_view()),
    ]

notes/views.py

    from django.views.generic import TemplateView

    class IndexPage(TemplateView):
        template_name = 'index.html'

notes/templates/home.html

    <!doctype html>
    <html lang="en">
        <head>
            <title>My Home Page</title>
        </head>
        <body>
            <h1>My Home Page</h1>
            <p>This page is hosted at Python Anywhere.</p>
            <p>Project #2 - BACS 350</p>
        </body>
    </html>


project01/settings.py

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'views/templates')],
            ...
        },
    ]

Terminal

    python manage.py runserver
    
    browse to http://localhost:8000
    

### Step 7 - Add an Image

notes/templates/home.html

    {% load static %}
    <!doctype html>
    <html lang="en">
        <head>
            <title>Page with Image</title>
        </head>
        <body>
            <h1>Home with Favicon</h1>
            <img src="{% static 'Bear.png' %}" alt="Bear Logo">
        </body>
    </html>


    

### Step 8 - Fix Favicon

project01/settings.py
    
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]


notes/templates/home.html

    {% load static %}
    <!doctype html>
    <html lang="en">
        <head>
            <title>Django Favicon Tutorial</title>
            <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        </head>
        <body>
            <h1>Home with Favicon</h1>
            <img src="{% static 'Bear.png' %}" alt="Bear Logo">
        </body>
    </html>

    
## Project Requirements

This demo code has ten requirements.   Your project code will have the same ten requirements.

* Your Github account is registered on the Sensei Server - Student Dashboard
* All code is checked into Github
* Has screen shot showing Python, Virtual Env, Django
* Screen shot of tree view showing Project 1 files
* Screen shot of running server

* Screen shot of http://localhost:8000 in browser
* Home page with Student Profile loading from template
* Student image loading from static directory
* Favicon loading
* Title set on browser tab

