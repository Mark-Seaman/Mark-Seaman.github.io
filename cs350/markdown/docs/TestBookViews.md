# How to Test Views with Data

Using the Django Test framework


### Data or No Data?
* If data operations are needed then use TestCase as the base class
* If no data operations are needed then use SimpleTestCase as the base class


```python
from django.test import SimpleTestCase, TestCase

# No data
class ViewsTests(SimpleTestCase)

# Book data
class BookViewsTests(TestCase)    
                            
```


### Test Book Views
* Test the views for the Book data model
* Views
    * book_list
    * book_add
    * book_edit
    * book_detail
    * book_delete
    

### Check for Page URL
* Get the URL that matches the view for the data model
* Book data must be tied to a user
* Create a fake user for testing
* Create a book object for all tests

```python
from django.contrib.auth import get_user_model
from django.test import TestCase

class BookViewsTests(TestCase):
    
    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def setUp(self):
        self.create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), '/book/1')

```


### Check List View
* Get the URL that matches the view for the data model
* Check that book_list page exists
* Check that book title is on page
* Check that check that book count is one
* Check that book_list.html template is used

```python
from django.test import TestCase

class BookViewsTests(TestCase):

    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def setUp(self):
        self.create_test_user()
        self.user = create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tale of Two Cities')
        self.assertContains(response, '<li>', count=1)
        self.assertTemplateUsed(response, 'book_list.html')

```


### Check Detail View
* Get the URL that matches the view for the data model
* Check that book_detail page exists for book 1
* Check that book title, author, description
* Check that book_list.html template is used
* Check for missing page

```python
from django.test import TestCase

class BookViewsTests(TestCase):

    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def setUp(self):
        self.create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)

    def test_book_detail_view(self):
        response = self.client.get('/book/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Charles Dickens')
        self.assertContains(response, 'Tale of Two Cities')
        self.assertContains(response, 'No description')
        self.assertTemplateUsed(response, 'book_detail.html')
        no_response = self.client.get('/book/100000')
        self.assertEqual(no_response.status_code, 404)

```


### Check Login
* Some views require login
* Use the TestCase.client to login to server
* Create user
* Check that user can login

```python
from django.test import TestCase


class BookViewsTests(TestCase):
    
    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def login(self):
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)
        
    def setUp(self):
        self.create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)
        self.login()
```


### Check Create View
* Create user, author, and book records
* Login to modify data
* Post data to "book_add" URL
* Count the books (should be two)
* Get the new book
* Check that book title, author, description

```python
from django.test import TestCase

class BookViewsTests(TestCase):

    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def setUp(self):
        self.create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)
        self.login()

    def test_book_create_view(self):
        new_book = dict(title="Sea Wolf", description='No big deal')
        response = self.client.post(reverse('book_add'), new_book)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Book.objects.all()), 2)
        book = Book.objects.last()
        self.assertEqual(book.author.name, 'Charles Dickens')
        self.assertEqual(book.title, 'Sea Wolf')
        self.assertEqual(book.description, 'No big deal')

```


### Check Update View
* Create user, author, and book records
* Login to modify data
* Post data to "book_edit" URL
* Count the books (should be one)
* Get the book
* Check that book title, author, description

```python
from django.test import TestCase

class BookViewsTests(TestCase):

    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def setUp(self):
        self.create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)
        self.login()

    def test_book_update_view(self):
        kwargs = dict(title='Lord of the Rings', description='Great story')
        response = self.client.post(reverse('book_edit', args='1'), kwargs)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Book.objects.all()), 2)
        b = Book.objects.get(pk=1)
        self.assertEqual(b.title, 'Lord of the Rings')

```


### Check Delete View
* Create user, author, and book records
* Login to modify data
* Post data to "book_delete" URL
* Count the books (should be one)

```python
from django.test import TestCase

class BookViewsTests(TestCase):

    def create_test_user(self):
        args = dict(username='TEST_DUDE', email='me@here.com', password='secret')
        self.user = get_user_model().objects.create_user(**args)

    def setUp(self):
        self.create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)
        self.login()

    def test_book_delete_view(self):
        response = self.client.post(reverse('book_delete', args='1'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Book.objects.all()), 0)

```
