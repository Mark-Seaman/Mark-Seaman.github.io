# Test Document

There are five unique levels of the test hierarchy.  
This document shows each level as a tree structure.
With each milestone we intend on building out a level of this test
plan.

## Planning Levels
* Level 1 - Test Plan
* Level 2 - Test Area
* Level 3 - User Story Test
* Level 4 - Test Script
* Level 5 - Test Case


## Test Hierarchy

* Manual Acceptance Testing
    * Views
        * Author Authentication
        * Author Registration
        * Create New Book
        * Show Books
        * Edit Book
        * Read Book
    * Database
    * User accounts
    * Reports
    * Diagnostics

* Quick Tests in development
    * Views
    * Database
    * Order processing
    * User accounts
    * Reports
    * Diagnostics

* Page Tests (using "requests" Python package on PyTest)
    * Views
    * Database
    * Order processing
    * User accounts
    * Reports
    * Diagnostics


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
    
    

#### Level 2 - Test Area

* This level outlines the testing that will occur on each major block of functionality.
* Product subsystems

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
