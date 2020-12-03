# Demo 1 - Development Tools

Application notes for learning about Web Hosting


## Steps to build demo code

Follow each of these steps carefully to produce the results that are
are required by this project.  

This project will require you to setup the development tools for local
editing on your computer system.

Follow each step until it is complete.  Do not continue on unless it
is correct.


### Step 1 - Install Python 3

    python --version
    
    python3 --version
    
Browse to python.org

Download Python 3

    python3 --version
    
    python3
    
    print('My name is Bob')
    

### Step 2 - Setup a Virtual Environment

    mkdir my-project-directory
    cd my-project-directory
    
    pip3 freeze
    
    python3 -m venv ./.venv
    
Mac - Activate Virtual Environment

    source ./.venv/bin/activate

Your terminal prompt should show "(.venv)" when you activate the environment

    (.venv) ~/Github/UNC-BACS-350
    
    
Windows - Activate Virtual Environment

    .venv/Scripts/activate.bat

Check your VENV

    pip freeze
    
    certifi==2018.10.15
    pipenv==2018.11.26
    virtualenv==16.1.0
    virtualenv-clone==0.3.0
    
Note that Django is missing
    
To deactivate the environment

    deactivate
    
Your terminal prompt should not show "(.venv)" when you deactivate the environment

    ~/Github/UNC-BACS-350
    

### Step 3 - Install Django

    pip install django
    
    pip freeze
    
    asgiref==3.2.10
    certifi==2018.10.15
    Django==3.0.8
    pipenv==2018.11.26
    pytz==2020.1
    sqlparse==0.3.1
    virtualenv==16.1.0
    virtualenv-clone==0.3.0
    
Note that Django 3.0.8 is installed
    

### Step 4 - Start a Django Project

    django-admin help
    
    django-admin startproject project1
    
    python manage.py help
    
    python manage.py runserver


### Step 5 - Start a Django App

    python manage.py startapp notes
    
project01/urls.py

    urlpatterns = [
        path('', index, name='index'),
    ]


notes/views.py

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("<h1>Hello, world.</h1> This is a simple HTML page.")


Terminal

Run the web server

    python manage.py runserver

Run Firefox or Chrome

    browse to http://localhost:8000
    

### Step 6 - Build a Template View

notes/views.py

    from django.views.generic import TemplateView

    class HomePageView(TemplateView):
        template_name = 'home.html'

    
project01/urls.py

    urlpatterns = [
        path('home', HomePageView.as_view(), name='home'),
    ]


notes/templates/home.html

    <!doctype html>
    <html lang="en">
        <head>
            <title>My First App</title>
        </head>
        <body>
            <h1>My First Django App</h1>
        </body>
    </html>


Terminal

    python manage.py runserver
    
    browse to http://localhost:8000/home
    

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


project01/settings.py

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'notes/templates')],
            ...
        },
    ]
    

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

