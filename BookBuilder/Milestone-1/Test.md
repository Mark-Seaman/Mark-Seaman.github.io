# Milestone 1. Project Plan Complete - Test


## PROJECT INFO

* [Software Project Plan - Book Builder](../Index.md)

* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: Milestone-1/Test.md

* URL: https://github.com/Mark-Seaman/Mark-Seaman.github.io/blob/master/BookBuilder/Milestone-1/Test.md

* Documents: Documents/swplan/BookBuilder

* Git Repo: Mark-Seaman.github.io


### Milestone 1. Project Plan Complete

Role: QA Engineer - Test

Goal: Test Plan

* Outline of testing that will be used
* Setup structure for testing
* Log issues
* Document how to log issues



## Book Builder - Test Plan

Each level of the hierarchy produces increasing levels of detail.  Test planning should always start at the top and work down. This prevents getting lost
in the weeds and running out of time.

A typical medium-sized app can be built in about 1000 hours of engineering time.  This means that about 250 hours should be spent on testing.  The
testing hierarchy acts as a natural budget for how to spent that time.


### Testing Levels 

This info is not specific to book builder but relates to test planning in general.


#### Level 1 - Test Plan

* High level discussion of testing strategy
* Outline the major types of testing that will be done
    * Manual Acceptance Testing - A person uses the application and observes what happens.  The test script describes scenarios that the tester must go through.
    * Django unit test - Automatic tests that may start with a blank database.  These tests can be very fine grained or run the entire system.
    * Hammer test - These tests execute automatic scenarios that exercise the entire system.
    * Quick test - The test is only used during development to iterate on a single function.
    * Page test - This test runs on “requests” Python package and gets web pages from a live server it is used to see if pages on the internet are changing.
    * Selenium Page test - Firefox and Chrome are used to obtain pages and look for specific HTML elements.
    
Book Builder testing

* Testing will be reduced because of limited time on this project.
* Essential testing will include
    * Manual Acceptance Testing
    * Quick Tests in development
    * Page Tests (using "requests" Python package on PyTest)
    

#### Level 2 - Test Area

* This level outlines the testing that will occur on each major block of functionality.
* Product subsystems
    * Views
    * Database
    * Order processing
    * User accounts
    * Reports
    * Diagnostics

#### Level 3 - User Story Test

* Each Test Area is decomposed into a number of User Stories.  
* Each User Story is defined as a User Experience (UX) that is documented in the requirements
* A User Story Test outlines how the UX scenario will be exercised and verified
* Examples:  Student Auth UX,  Create New Book UX, Register Student Grade UX

#### Level 4 - Test Script

* Each User Story  is decomposed into a number of User Scenarios.  
* A Test Script outlines how the User Scenario will be exercised and verified.
* Examples:  Student Auth UX
    * Student can register
    * Student can login
    * Student can logout
    * Only students can see grades

#### Level 5 - Test Case

* Each User Scenarios  is decomposed into a number of specific features that the app implements.  
* A Test Case outlines specific behavior to be exercised and what the expected results are.
* Examples:  Students can register
    * Successful registration
    * Error for bad email, name, or already enrolled
    * Student can login after registering
    * Errors prevent student from being enrolled


## Hierarchy of Test Details

### Complete Test Plan

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (7-10)
* Level 3 - User Story Tests (50-100)
* Level 4 - Test Scripts (200-400)
* Level 5 - Test Cases (1000-2000)

### Essential Test Plan

This task can seem overwhelming if you look at the whole.   We will be using a essential planning strategy at the start of the project to focus on the core testing first.  If we have time later we can add in more testing.

While every item in the hierarchy may have 5-10 legitimate children, they are not all equally important.  Our essential test plan forces us to select the four most important items at every level.  This gives a robust plan for test what is truly important.  Compare the number of artifacts to the complete plan above.  Instead of detailing 2000 Test Cases we are only dealing with 250.

Book Builder Testing Hierarchy

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (4)
* Level 3 - User Story Tests (16)
* Level 4 - Test Scripts (64)
* Level 5 - Test Cases (256)

Over the course of the project we plan to spend about 250 hours testing and can focus on the 250 Essential Test Cases.  This makes testing totally predictable and manageable.  If there is enough time you can do more but you are guaranteed to get the most important stuff tested.


## User Auth - Test Script

Manual Testing - live user clicking buttons

Test Cases - Student Auth

* Scenario 1 - Guest Access
    * Guests can see system view with Welcome
    * Not logged in displayed
    * Menu has links to Authors, Books, Chapters, Review

* Scenario 2 - Register New Author
    * Author can register
    * Error for used email
    * New users are created
    * Dropping a Author removes the user record
    * Existing user records are used

* Scenario 3 - Author Access
    * Author can log in successfully
    * Author can see course view with Student Settings and Welcome
    * Login displayed
    * Logout menu item
    * Menu has links to Authors, Books, Chapters, Review
    * Books shows all current books
    * Chapters shows all current chapters
    * Docs shows all current docs
    * Dropped Authors can not log in

* Scenario 4 - Reader Access
    * Private books require readers to register
    * A user access list shows content for specific readers


### Setup structure for testing

The book builder project will start by doing manual testing only.  This means for the
first two milestones we do not need to have any specific infrastructure for automated
testing.

The above test scripts cover the scope and high level direction that the testing will 
take.  An example Level 4 - Test Script has been included to illustrate the kind of 
Test Scripts that will be developed later on in the project.

All five level of the testing hierarchy will be documented in the [Test Documents](../docs/TestDocs) area of our website.


### Log issues

The Github issues tracking system will be used to track all known items and remaining
work.

The Product Backlog will be an Issue in the BookBuilder project.  It will track the 
priorities for the current Sprint.  The functionality that is expected for the next
milestone will be documented in the Product Backlog.

At the end of the Milestone all work listed in the Product Backlog must be complete.
Any unresolved issues must be logged within the Github issues list.

