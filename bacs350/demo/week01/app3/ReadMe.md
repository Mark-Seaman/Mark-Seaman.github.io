# Skill #3 - Serve Static Images

This is the world's simplest web app

Follow these steps to build it yourself

Create the project

    django-admin startproject app3
    
    tree

Create HTML templates

    mkdir templates
    
Edit app3/settings.py  to load the templates

    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ...
        },
    ]

Create templates/home.html

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>Home</title>
    </head>

    <body>
        <h1>Trees</h1>
        <p>
            <a href="about">About Us</a>
        </p>
        <p>
            <img src='/static/img/treetops.200.jpg'>
        </p>
    </body>

    </html>

Create templates/about.html

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>About</title>
    </head>

    <body>
        <h1>Bear</h1>
        <p>
            <a href=".">Go Home</a>
        </p>
        <p>
            <img src='/static/img/Bear.200.png'>
        </p>
    </body>

    </html>

Edit pages/views.py

    from django.views.generic import TemplateView


    class HomeView(TemplateView):
        template_name='home.html'

    class AboutView(TemplateView):
        template_name='about.html'

Edit app3/urls.py
    
    from django.urls import path

    from pages.views import AboutView, HomeView

    urlpatterns = [
        path('', HomeView.as_view()),
        path('about', AboutView.as_view()),
    ]

Test the application

    python ./manage.py runserver
    
    browse to http://127.0.0.1:8001/

Fix the broken images by using a static server

Edit settings.py

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

    
Now you do it!

