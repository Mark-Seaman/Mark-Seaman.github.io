# Code Structure


## App Settings

tree bookbuilder
    
    .
    ├── book
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── bookbuilder
    │   ├── asgi.py
    │   ├── settings.py
    │   └── wsgi.py
    ├── templates
    ├── db.sqlite3
    └── manage.py
    
    
The [settings.py](../bookbuilder/bookbuilder/settings.py) file runs the app startup.

This is in the "bookbuilder" app folder.

Startup files are "asgi.py" and "wsgi.py" and "manage.py".

Data migrations folder contains all the database migration history.


## Book App

The Django Book Builder project has one Django app called "book".

"book" holds 

* the data models ([models.py](../bookbuilder/book/models.py))
* the views for books and users ([views.py](../bookbuilder/book/views.py))
* the URL routes ([urls.py](../bookbuilder/book/urls.py))


## HTML Templates

* All HTML template files are located in "templates" folder

