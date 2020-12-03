# Book Builder Data Models

## Book Builder Data

Data Classes and database tables

* Reader
    * user*
* Author
    * user*
    * name
* Book
    * author*
    * title
* Chapter
    * book*
    * title
    * order
    * text

“*” makes a link to another table.  This is implemented 
by a foreign key relationship between the two tables.  

Example: Books have Authors so the Book data model has
a ForeignKeyField that points to the Author Model class.

#### book/models.py

bookbuilder/settings.py

    INSTALLED_APPS = [
        ...
        'book',
    ]

book/models.py

    from django.db import models
    from django.contrib.auth.models import User

    class Author(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)

    class Book(models.Model):
        user = models.ForeignKey(Author, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)

Migrate the database

    python manage.py makemigrations
    
    python manage.py migrate
 
 
## Django Admin Views

Enable the admin views

book/urls.py

    from django.urls import path
    from django.contrib import admin

    urlpatterns = [
        path(r'admin/', admin.site.urls),
    ]
    

book/admin.py

    from django.contrib import admin
    from .models import Author, Book

    admin.site.register(Author)
    admin.site.register(Book)

Create Superuser to use admin views

    python manage.py createsuperuser
    
    python manage.py runserver
    
Browse to test

    Visit http://127.0.0.1:8002/admin/
    
    
## Book Builder Data Models

* [book/models.py](../bookbuilder/book/models.py)

