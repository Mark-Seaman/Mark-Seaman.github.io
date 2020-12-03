# Code Design Pattern Catalog

Design Patterns are the key to great engineering

Every Web App requires 50 Tricks


### App Structure

A new Django project is created by running a script that builds code for
the project.

    django-admin startproject Book-Builder
    
Application modules are created for unique functional areas of the program.

    python manage.py startapp book
    

### Template Views

The base view class in Django is TemplateView.  This displays HTML code
for the required template.  The settings file must contain the location
of the template.

Template View Example

    class HeroEditView(TemplateView):
        template_name = "hero.html"


### View Inheritance

Define a base page template.  Then extend the template by replacing
the desired blocks of HTML text.

templates/theme.html

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    
templates/home.html

    {% extends 'theme.html' %}

    {% block content %}
        <h1>Home Page</h1>
        <p>This is the page.</p>
    {% endblock content %}



### Data View 

Django defines several generic view types that automatically present
data records from a database. The developer must define the operation
to be done, the HTML template, and the data model.

Edit View Example

    class HeroEditView(CreateView):
        template_name = "hero_edit.html"
        model = Superhero
        fields = '__all__'

Django View Classes

* TemplateView
* ListView
* DetailView
* CreateView
* UpdateView
* DeleteView


### Data Models

The ORM takes a python class and automatically builds database tables
that match the database model.  As the model changes the database tables
are altered using a migrate process.


hero/models.py

    class Superhero(models.Model):
        name = models.CharField(max_length=20)
        identity = models.CharField(max_length=20)

Migrating the Database

    python manage.py makemigrations
    
    python manage.py migrate
    
    

### Data Functions

Encapsulate database access functions with friendly names that
can be easily remembered.  Create functions for the most common
queries needed.

book/book.py

    from .models import Book

    def add_book(title, author):
        return Book.objects.create(author=author, title=title)

    def list_books(author=None):
        return Book.objects.all()

    def get_book(title):
        return Book.objects.get(title=title)

    def get_book_id(pk):
        return Book.objects.get(pk=pk)

    def delete_book(title):
        Book.objects.get(title=title).delete()



### App Hosting

Use Python Anywhere to host Django apps.  Signup for the free version of 
the service.

Follow the [Python Anywhere setup guide](PythonAnywhere) to configure server.



### Markdown Content

Display document content written in markdown as HTML text.  Include a markdown
formatter from the Python package (markdown).

See [Markdown Design Pattern](Markdown.md)

