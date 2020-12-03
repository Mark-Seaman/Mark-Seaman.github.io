# Test Driven Development

Using TDD for Book Builder Data


### Test-driven Development Setup
* Developer tools setup
* Github Desktop
    * View changes
    * Commit and changes
    * Pull new code
* Run Editor
    * Use Open Folder in Brackets to remember code location
    * Remember last change made
* Run a terminal window
    * Verify the virtual environment
    * Run the server
    * Test the code
    * Fix any errors
    
    
### Workflow for Development
* Pull code
* Feature Loop (focus on one feature)
    * Create a failing test
    * Create the code to pass the test
    * Save the test code for later
    * Commit and push changes
    * Select next feature
* Run all tests
* Fix all defects
* Push code


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
* Paragraph
    * chapter*
    * text
    * order
* Image
    * chapter*
    * src
    * alt
    * order

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
 
 
book/tests.py
 
    class AuthorTests(TestCase):

        def test_author_model(self):
            self.assertEqual(len(Author.objects.all()), 0)

Test iterations

Test 1 - No Authors

    self.assertEqual(len(Author.objects.all()), 0)

Test 2 - Create One Author

    def test_create_author(self):
        user = get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret')
        author = Author.objects.create(user=self.user, name='Charles Dickens')
        self.assertEqual(len(Author.objects.all()), 1)

Test 3 - Check Author Name

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret')
        self.author = Author.objects.create(user=self.user, name='Charles Dickens')

    def test_author_model(self):
        self.assertEqual(self.author.name, 'Charles Dickens')
        self.assertEqual(self.author.user.username, 'TEST_DUDE')
    
Test 4 - Add Author
     
        def test_create_author(self):
            self.assertEqual(len(Author.objects.all()), 1)
            a = Author.objects.create(user=self.user, name='Jack London')
            self.assertEqual(len(Author.objects.all()), 2)
            self.assertEqual(a.name, 'Jack London')
            self.assertEqual(a.user.username, 'TEST_DUDE')

Test 5 - List Authors
    
        def test_list_authors(self):
            self.assertEqual(len(Author.objects.all()), 1)
            self.assertEqual(Author.objects.get(name='Charles Dickens').name, 'Charles Dickens')
    
Test 6 - Update Author

        def test_update_author(self):
            a = Author.objects.get(pk=1)
            self.assertEqual(a.name, 'Charles Dickens')
            a.name = 'George Orwell'
            a.save()
            a = Author.objects.get(pk=1)
            self.assertEqual(a.name, 'George Orwell')
    
Test 7 - Delete Author

        def test_delete_author(self):
            a = Author.objects.get(pk=1)
            a.delete()
            self.assertEqual(len(Author.objects.all()), 0)

Refactor

book/author.py

    def add_author(user, name):
        return Author.objects.create(user=user, name=name)
        
    def list_authors():
        return Author.objects.all()
        
    def get_author(name):
        return Author.objects.get(name=name)
        
    def delete_author(name):
        Author.objects.get(name=name).delete()

        
book/tests.py

    def check_author_name(self, pk, name):
        a = Author.objects.get(pk=pk)
        self.assertEqual(a.name, name)
        
    def check_author_user(self, pk, username):
        a = Author.objects.get(pk=pk)
        self.assertEqual(a.user.username, username)
        
    def check_num_authors(self, num):
        self.assertEqual(len(list_authors()), num)
       
    def create_test_user(self):
         self.user = get_user_model().objects.create_user(
            username='TEST_DUDE', 
            email='me@here.com', 
            password='secret'
         )
        
Refactored Tests

    def create_test_user():
        return get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret')

    class AuthorTests(TestCase):
    
        def check_author_name(self, pk, name):
            a = Author.objects.get(pk=pk)
            self.assertEqual(a.name, name)
    
        def check_author_user(self, pk, username):
            a = Author.objects.get(pk=pk)
            self.assertEqual(a.user.username, username)
    
        def check_num_authors(self, num):
            self.assertEqual(len(list_authors()), num)
    
        def setUp(self):
            self.user = create_test_user()
            self.author = add_author(self.user, 'Charles Dickens')
    
        def test_author_model(self):
            self.check_num_authors(1)
            self.check_author_name(1, 'Charles Dickens')
            self.check_author_user(1, 'TEST_DUDE')
    
        def test_create_author(self):
            self.check_num_authors(1)
            add_author(self.user, 'Jack London')
            self.check_author_name(2, 'Jack London')
            self.check_author_user(2, 'TEST_DUDE')
            self.check_num_authors(2)
    
        def test_list_authors(self):
            self.check_num_authors(1)
            self.assertEqual(get_author('Charles Dickens').pk, 1)
    
        def test_update_author(self):
            self.check_num_authors(1)
            a = get_author('Charles Dickens')
            a.name = 'George Orwell'
            a.save()
            self.check_author_name(1, 'George Orwell')
    
        def test_delete_author(self):
            delete_author('Charles Dickens')
            self.check_num_authors(0)
