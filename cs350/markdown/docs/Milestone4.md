# Functionality Complete Milestone 

Design Review and Status Update


## Software Lifecyle

### Requirements 

Readers do not need to login.   This simplifies the user management.

Have not yet implemented the user registration system.  We plan to
do that next week.


### Design 

Original plan was to create Chapter data model that includes Paragraph and Image.
This can be simplified by adding a "text" field to Chapter that contains Markdown
text.  This allows a fully formatted document to be a standard part of every
Chapter record.

Documented the [design patterns](DesignPatterns.md) being used.


### Code 

Build standard set of views and navigation.

* Author - List, Detail, Create, Update, Delete   (these views are not yet implemented)
* Book - List, Detail, Create, Update, Delete  (fully functional except for Delete)
* Chapter - List, Detail, Create, Update, Delete  (fully functional except for Delete)

Each view:

* model
* template
* view
* url


### Test 

Broke tests into separate files.

Removed "View Prototype" tests since View Prototype code was removed.

Issues (neglected to log issues, will follow up on that next week)

