# Prototype Views

This simple application is used to illustrate the general flow
of the views in the finished application.  The main purpose of 
building a prototype app for the views is to have a robust 
conversation between the developers and the client.

A sketch (or wireframe diagram) is not real enough.  And waiting
for the real app to be built out introduces a huge delay in the project.
To be useful the prototype must be both quick and realistic.

* Create an app to illustrate the views
* Everything is fake
* Views have no style
* Show the user flow and navigation
* Limit the time spend to 4 hours
* Build a reusable app to show HTML files

The prototype is a simple app that displays a series of HTML pages.
Each page represents a view in the final application. Text is added
to the view to illustrate the contents that will be in the view.

Hyperlinks are used to sequence between the views so that the 
client can evaluate the user experience that will be built out
later in the project.


### Book Builder App Views

To illustrate how to build a view prototype let's look at the 
Book Builder project.   There are a number of different views
that will be built.

* Users
    * Register Author
    * Register Reader
    * Login
    * Logout
* Books
    * Create Book
    * List Books
    * Edit Book
    * Read Book
    * Delete Book
* Chapters
    * New Chapter
    * Edit Chapter
    * Read Chapter
    * Delete Chapter
    
For each of these views we build the simplest possible HTML code
that captures the essence of what will happen in the view.  While 
the eventual view will be dynamically created we don't want to 
worry about any of that now.

We hard-code all text directly into the HTML templates so that
we can get something that look real enough at a small fraction of the
cost.  Our goal is to spend no longer than 15 minutes per view created.


### Book Builder View Templates

Visit the [View Templates](https://github.com/Mark-Seaman/Book-Builder/tree/master/bookbuilder/templates)
to see the implementation of the book builder prototype.

List of HTML files

    delete_book.html
    delete_chapter.html
    edit_book.html
    edit_chapter.html
    index.html
    list_books.html
    login.html
    logout.html
    missing.html
    read_book.html
    read_chapter.html
    register_author.html
    register_reader.html


### Template Pages Viewer

Use one URL Route to load different Page Templates.  The following code
snippets show how to get pages displayed directly from HTML files
for Django apps.


#### pages/views.py

    from django.views.generic import TemplateView
    
    class PageView(TemplateView):
    
        def get_template_names(self):
            template_name = self.kwargs.get('template')
            return template_name
        

#### urls.py

    from django.urls import path
    from page.views import PageView
    
    urlpatterns = [
        path('<str:template>', PageView.as_view()),
    ]
    

