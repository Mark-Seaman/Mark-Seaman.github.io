# Book Builder Development Log

There are several goals that must be met on the Book Builder project.

Here is a log of recent activity and notes for later.

---


## Goals  10-25

* Rebuild Virtual Env  (Installed Python 3.8.6)
* Add user administration
* Update Data Models (Author, Book, Chapter)
* Testing


### Rebuild Virtual Env
* [Rebuild Virtual Env](RebuildVenv.md)
    
 
### Add user administration
* [Users accounts](UserAccounts.md)
* Register
* Login/logout
* Require login
* Show login info


### Update Data Models
* Testing
    * dj test
    * Basic user tests
* Known Problems
    * Author
        * Authors are currently hard code to Author 1
        * Need to create views to add and edit new authors
        * Tie author to logged in user
    *  Book
        * Works correctly
    *  Chapter
        * Tie add chapter to a specific book

---


## Goals  10-27

* Setup Dev Context
* Rename app settings folder
* Deploy & test code
* Use View Inheritance
* Known Problems


### Setup Dev Context
* Define a script that sets up the dev environment and tools
* [start development script](../start)


### Rename app settings folder
* mv bookbuilder config
* Edit files (manage, asgi, wsgi, settings)
* dj test
* dj runserver


### Deploy & test code

* Test locally (auto, manual)
* Commit and push
* Pull and bounce server 
* Test remotely
* [Update Server](UpdateServer.md)

    
### Use View Inheritance

Create a series of templates
    
    book_theme.html
    _header.html
    _footer.html
    _navbar.html
    _user.html
    
[View Templates](ViewInheritance.md)


### Improve Appearance
* Use logic from Shrinking World website
    * Header with globe banner art
    * CSS stylesheet (static/shrinking-world.css)
    * Body background (static/paper.png)
    * Set text color to dark
    
---


## Goals  10-29

* Description for book
* Book for chapter
* Add and edit authors
* Author for book
* Favicon - Setup book icon



### What Next?

* **TEST**  (current state)
    - dj test, dj runserver
    - Create tests find problems and log issues
* **FIX**  (known problems)
    - Fix known issues
* **EXTEND**  (new features)
    - Create features with tests
* **IMPROVE**  (simplify)
    - Refactor to eliminate duplication
    - Refactor Django tests


### Test
* dj test
* dj runserver


### Known Problems
* Description for book
* Book for chapter
* Add and edit authors
* Author for book
* Favicon - Setup book icon
* Automatically set chapter numbers


### Description for book
* Detail View pass in markdown HTML and display
* Modify book/models.py
* Modify book/views.py
* Modify templates/book_detail.html
* Modify book/tests.py


### Set Book for chapter
* Remove the book field from forms for add or edit
* Pass in the book Id when creating a new chapter
* Set the book Id in the form when saving the record

```python
# models.py
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    chapter_num = models.IntegerField()
    text = models.TextField(default='No Chapter Text')

    
# urls.py
urlpatterns = [
    # Pass the book id
    path('chapter/<int:book_id>/add', ChapterAdd.as_view(),     name='chapter_add'),
]


# views.py
class ChapterAdd(LoginRequiredMixin, CreateView):

    template_name = "chapter_add.html"
    model = Chapter
    fields = '__all__'

    def form_valid(self, form):
        book_id = self.kwargs.get('book_id')
        form.instance.book_id = book_id
        return super().form_valid(form)
```


### Favicon - Setup book icon
* Copy the Bear Icon and the Shrinking World icon to /static
* In the base template load the static files and set the icon

```html
{% load static %}

<!doctype html>
<html lang="en">
    <head>
       ...
        <link rel="stylesheet" href="/static/shrinking-world.css">
        <link rel="shortcut icon" type="image/png" href="{% static 'Bear.favicon.ico' %}"/>
    </head>
```


### Test View Without Data
* Test the views for proper structure
* This tests looks a pages without any data
* [Test Views](TestViews.md)
* [View Tests Code](https://github.com/Mark-Seaman/Book-Builder/blob/master/bookbuilder/book/tests.py)


### Test Book Views
* Test the views for the Book data model
* Views
    * book_list
    * book_add
    * book_edit
    * book_detail
    * book_delete
* [Test Book Views](TestBookViews.md)
* [Book Tests Code](https://github.com/Mark-Seaman/Book-Builder/blob/master/bookbuilder/book/tests_book.py)


### Deploy & test code

* Test locally (auto, manual)
* Commit and push
* Pull and bounce server 
* Test remotely
* [Update Server](UpdateServer.md)



---

## Remaining Tasks

### Known Problems

### Extend (new features)

### Improve  (simplify)
