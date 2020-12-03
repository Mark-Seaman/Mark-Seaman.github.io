# Deploy & test code

Test locally (auto, manual)

* dj test
* Basic user tests

Commit and push

    co "Rename app settings folder to config"
    

Pull and bounce server

    Login to Python Anywhere console
        
        cd /home/markseaman/Book-Builder
        
        git pull
        
    Migrate the database
    
        python manage.py makemigrations
        
        python manage.py migrate
        
    Browse to WebApp config
    
    Edit the WSGI.py
        
        # +++++++++++ DJANGO +++++++++++
        # To use your own django app use code like this:
        import os
        import sys

        ## assuming your django settings file is at '/home/markseaman/Book-Builder/bookbuilder/config/settings.py'
        ## and your manage.py is is at '/home/markseaman/Book-Builder/bookbuilder/manage.py'
        path = '/home/markseaman/Book-Builder/bookbuilder'
        if path not in sys.path:
            sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()


    Reload server
    
    Browse to http://markseaman.pythonanywhere.com


Test remotely

    dj test
    
    Basic user tests
    