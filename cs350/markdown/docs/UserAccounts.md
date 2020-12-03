# Book Builder - User Accounts

Tasks to complete

    Use the accounts app developed in BACS 350 - Demo 26
    Hook up to Book Builder
    Require login for Edit, Add, Delete
    Test with Book Editing

Use the accounts app developed in BACS 350 - Demo 26

    dj startapp accounts
    
    cp /Users/seaman/Github/UNC-BACS-350/demo/week10/Demo29/accounts/* accounts
    
    cp /Users/seaman/Github/UNC-BACS-350/demo/week10/Demo29/templates/registration/* templates/registration

bookbuilder/settings.py

    INSTALLED_APPS = [ ... 'accounts' ]
    STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
    
    LOGIN_REDIRECT_URL = ''
    LOGOUT_REDIRECT_URL = '' 

book/views.py

    from django.contrib.auth.mixins import LoginRequiredMixin
    
    class BookAdd(LoginRequiredMixin, CreateView):
    
    class BookEdit(LoginRequiredMixin, UpdateView):
    
    dj runserver -- test the add and edit book

fix base page "book_theme.html"