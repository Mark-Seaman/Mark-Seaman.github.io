# Skill #1 - Build and Serve Simple Pages

This is the world's simplest web app

Follow these steps to build it yourself

Create the project

    django-admin startproject app1
    
    tree
    
Edit app1/urls.py
    
    from django.http import HttpResponse
    from django.urls import path


    def home_page_view(request):
        return HttpResponse("<h1>World's Simplest Website</h1>")


    urlpatterns = [
        path('', home_page_view),
    ]

Test the application

    python ./manage.py runserver
    
    browse to http://127.0.0.1:8001/
    
Now you do it!

