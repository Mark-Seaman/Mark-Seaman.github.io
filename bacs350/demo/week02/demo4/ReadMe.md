# Skill #4 - Create Pages from Templates

This is the world's simplest web app

Follow these steps to build it yourself

Create the project

    django-admin startproject demo4
    
    tree

Create HTML templates

    mkdir templates
    
Edit demo4/settings.py  to load the templates

    TEMPLATES = [
        {
            ...
            'DIRS': ['templates'],
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
        <h1>Home</h1>
    </body>

    </html>

Edit demo4/urls.py
    
    from django.views.generic import TemplateView
    from django.urls import path

    class HomeView(TemplateView):
        template_name='home.html'

    urlpatterns = [
        path('', HomeView.as_view()),
    ]

Test the application

    python ./manage.py runserver
    
    browse to http://127.0.0.1:8001/
    
Add pages app

    python ./manage.py startapp pages
    
    tree
    
Move code from demo4/urls.py to pages/views.py

    from pages.views import HomeView
    
Add templates/about.html

Add AboutView to pages/views.py

Add route for 'about' to demo4/urls.py

    
Now you do it!

