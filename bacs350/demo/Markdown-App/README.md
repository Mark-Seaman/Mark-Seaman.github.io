# Markdown Display

Application notes for learning about using Markdown within Django.




## Steps to build demo code

Follow each of these steps carefully to produce the results that are
are required by this project.  

This project will require you to setup the development tools for local
editing on your computer system.

Follow each step until it is complete.  Do not continue on unless it
is correct!


### Step 1 - Start a Django Project

Begin Project 2 when you have fully completed Project 1

Activate your virtual environment

Start app36
    
    django-admin startproject app36
    python manage.py migrate 
    python manage.py runserver
    
Browse to http://localhost:8000 for the Django test page


### Step 2 - Build the notes Django App

Copy notes app and static files from previous project

Modify settings.py

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

    INSTALLED_APPS = [
        ...
        'notes',
    ]
    
Terminal

    Browse to http://localhost:8000 for the notes application pages
    

### Step 3 - Add Pagedown code

Go to terminal

    pip install django-pagedown
    
    pip list
    
    asgiref              3.2.10    
    certifi              2018.10.15
    Django               3.0.8     
    django-crispy-forms  1.7.2     
    django-markdown-deux 1.0.5     
    django-pagedown      0.1.3     
    markdown2            2.3.9     
    pip                  18.1      
    pipenv               2018.11.26
    pytz                 2020.1    
    setuptools           40.6.2    
    sqlparse             0.3.1     
    virtualenv           16.1.0    
    virtualenv-clone     0.3.0     
    wheel                0.32.3    

Visit Pagedown website

    [Pagedown website](https://github.com/timmyomahony/django-pagedown)
    
Checkout Video (if you get stuck)

    [Tutorial Video](https://www.youtube.com/watch?v=N6UM76OzjuM)

Edit settings.py

    INSTALLED_APPS = [
        ...
    
        #Third Party Apps
        'pagedown',
        
        # My Apps
        'notes',
    ]
    
### Step 4 - Build Note view

notes/views.py

    from django import forms
    from pagedown.widgets import PagedownWidget
    
    class NoteForm(forms.ModelForm):
    name = forms.CharField(widget=PagedownWidget())
    description = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Note
        fields = ["name"]
        
        
    
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

