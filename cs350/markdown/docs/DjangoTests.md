# Django Tests

Django is a web framework for perfectionists with deadlines.  It comes with batteries included.

One of the huge benefits of using Django is the direct support for testing via the test framework.


### Defining Tests

Here is a simple test that fetches the root page of this site and checks for a status code
of 200.

book/tests.py

    from django.test import SimpleTestCase
    
    class SimpleTests(SimpleTestCase):

        def test_home_page_status_code(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
    
        def test_about_page_status_code(self):
            response = self.client.get('/book_list.html')
            self.assertEqual(response.status_code, 200)


Create a test class that inherits from **SimpleTest**. This makes you test visible to Django test.  It
will be automatically executed from that point.

Define a series of specific tests as methods within the SimpleTest class.  These methods start with
**test_**.

Fetch web pages from your app by calling "self.client.get". This performs an HTTP GET operation
for the requested page.  For example, "/" or "/book_list.html".

Look in the response for the "status_code" and make sure that it is "200".


### Running Tests

A django script runs all of the tests defined inside all of the installed apps within the
project.

    python manage.py test
    
If any test fails the reason is shown so that it can be quickly fixed.  A good test is two
or three lines of code that tests one thing.  Writing simple tests makes it easy to produce
test code and maintain it. 

Tests should be run before committing code.  Tests should be written before writing code.



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


### Book Builder Tests

On Book Builder we will write tests that make page requests for each view in our project.
These will be written as we create views to remove any development burden.  Each test will
check to make sure that the page is available and that the correct HTML template is used.

* See code for [Book Builder Tests](https://github.com/Mark-Seaman/Book-Builder/tree/master/bookbuilder/book/tests.py)
* Link to [Code for Book Builder](https://github.com/Mark-Seaman/Book-Builder/tree/master/docs/plan/Milestone-2/Code.md)

