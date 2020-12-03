# Manual Testing - live user clicking buttons

Test Cases - Student Auth

* Scenario 1 - Guest Access
    * Guests can see course view with Welcome
    * Not logged in displayed
    * Menu has links to Course, Lessons, Docs, Projects

* Scenario 2 - Register New Student
    * Students can register
    * Error for used email
    * New users are created
    * New students records are added to class
    * Dropping a student removes the user record
    * Existing user records are used for second class

* Scenario 3 - Student Access
    * Students can log in successfully
    * Students can see course view with Student Settings and Welcome
    * Login displayed
    * Logout menu item
    * Menu has links to Course, Lessons, Docs, Projects
    * Lessons shows all current lessons
    * Projects shows all current projects
    * Docs shows all current docs
    * Dropped Students can not log in

* Scenario 4 - Teacher Access
    * Login as Mark Seaman goes to teacher view
    * Each class shows roster of students
    * User list shows enrollment
    * Login displayed
    * Logout menu item
    * Menu has links to Course, Lessons, Docs, Projects
    * Lessons shows all current lessons
    * Projects shows all current projects
    * Docs shows all current docs
