# Writing a Test Plan

Each level of the hierarchy produces increasing levels of detail.  Test planning should always start at the top and work down. This prevents getting lost
in the weeds and running out of time.

A typical medium-sized app can be built in about 1000 hours of engineering time.  This means that about 250 hours should be spent on testing.  The
testing hierarchy acts as a natural budget for how to spent that time.

## Planning Levels

### Level 1 - Test Plan

* High level discussion of testing strategy
* Outline the major types of testing that will be done
    * Manual Acceptance Testing - A person uses the application and observes what happens.  The test script describes scenarios that the tester must go through.
    * Django unit test - Automatic tests that may start with a blank database.  These tests can be very fine grained or run the entire system.
    * Hammer test - These tests execute automatic scenarios that exercise the entire system.
    * Quick test - The test is only used during development to iterate on a single function.
    * Page test - This test runs on “requests” Python package and gets web pages from a live server it is used to see if pages on the internet are changing.
    * Selenium Page test - Firefox and Chrome are used to obtain pages and look for specific HTML elements.

### Level 2 - Test Area

* This level outlines the testing that will occur on each major block of functionality.
* Product subsystems
    * Views
    * Database
    * Order processing
    * User accounts
    * Reports
    * Diagnostics

### Level 3 - User Story Test

* Each Test Area is decomposed into a number of User Stories.  
* Each User Story is defined as a User Experience (UX) that is documented in the requirements
* A User Story Test outlines how the UX scenario will be exercised and verified
* Examples:  Student Auth UX,  Create New Book UX, Register Student Grade UX

### Level 4 - Test Script

* Each User Story  is decomposed into a number of User Scenarios.  
* A Test Script outlines how the User Scenario will be exercised and verified.
* Examples:  Student Auth UX
    * Student can register
    * Student can login
    * Student can logout
    * Only students can see grades

### Level 5 - Test Case

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

This hierarchy can be documented to highlight the key artifacts.

* Level 1 - Test Plan (1)
* Level 2 - Test Areas (4)
* Level 3 - User Story Tests (16)
* Level 4 - Test Scripts (64)
* Level 5 - Test Cases (256)

Over the course of the project we plan to spend about 250 hours testing and can focus on the 250 Essential Test Cases.  This makes testing totally predictable and manageable.  If there is enough time you can do more but you are guaranteed to get the most important stuff tested.
