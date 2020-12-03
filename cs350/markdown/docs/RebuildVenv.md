# Book Builder - Rebuild Virtual Env

When updating to Python 3.8 my development environment became broken

I deleted the old environment and rebuilt it from scratch.

    cd ~/Github/Book-Builder/bookbuilder
    
    rm -rf 
    
    
Create new env

    python3 -m venv .venv
    
    source $code/.venv/bin/activate
    
    pip install --upgrade pip
    
    pip install django pillow markdown django-crispy-forms requests
    
    pip freeze
    
        asgiref==3.2.10
        certifi==2020.6.20
        chardet==3.0.4
        Django==3.1.2
        django-crispy-forms==1.9.2
        idna==2.10
        Markdown==3.3.2
        Pillow==8.0.1
        pytz==2020.1
        requests==2.24.0
        sqlparse==0.4.1
        urllib3==1.25.11
        
    # Setup alias   dj
    alias dj="python manage.py"
    
    dj test
    
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        ................
        ----------------------------------------------------------------------
        Ran 16 tests in 1.917s
        
        OK

    dj runserver
    
        Watching for file changes with StatReloader
        Performing system checks...
        
        System check identified no issues (0 silenced).
        October 25, 2020 - 19:57:21
        Django version 3.1.2, using settings 'bookbuilder.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
    
 Test in browser
 
 