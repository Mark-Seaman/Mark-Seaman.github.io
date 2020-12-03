# Deploy App on Python Anywhere

### Setup Python Anywhere Web App
* Follow steps in [Setup Python Anywhere](PythonAnywhere.md)

### Create Book Builder App
* Create [Book Builder Repo](GithubRepo.md)
* Create application code
* Commit to [Book-Builder](https://github.com/Mark-Seaman/Book-Builder)


### Clone Repo at PythonAnywhere
* Run Console at [PythonAnywhere](https://www.pythonanywhere.com/user/markseaman/)
* Clone the repo

    cd
    git clone https://github.com/Mark-Seaman/Book-Builder
    

### Allowed Hosts

Allow connection as Python Anywhere

settings.py

    ALLOWED_HOSTS = ['markseaman.pythonanywhere.com']


### Git Pull

    cd Book-Builder
    git pull   # Brings in new code
    
### Reload Server

    Visit page https://www.pythonanywhere.com/user/markseaman/
    
    View error logs
    

### Collect Static Media

In order to use the Admin views in Django you must gather up the
CSS, Image, and JavaScript files that the code needs. If you don't
set this up properly then the media will be missing from the views.

We set up the static media in the settings file. This causes the static
media to be served from the "app directory/static".

bookbuilder/settings.py

    STATIC_URL = '/static/'
    STATICFILES_DIRS = ['static']
    
    # Path to put additional files to be served (eg. Admin pages)
    STATIC_ROOT = '/home/markseaman/Book-Builder/bookbuilder/static'
    
Collect the static media on the production server.

    python manage.py collectstatic

When this is properly configured the admin views will appear properly styled.

