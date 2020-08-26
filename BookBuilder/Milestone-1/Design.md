# Milestone 1. Project Plan Complete - Design


## PROJECT INFO

* [Software Project Plan - Book Builder](../Index.md)

* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: Milestone-1/Design.md

* URL: https://github.com/Mark-Seaman/Mark-Seaman.github.io/blob/master/BookBuilder/Milestone-1/Design.md

* Documents: Documents/swplan/BookBuilder

* Git Repo: Mark-Seaman.github.io




### Milestone 1. Project Plan Complete



Role: Designer - Design

Goal: Technology selection

* Select Development Tools
* Infrastructure - Frameworks & Tools
* Setup Guide
* Create "Hello World"
* Decide on App deployment



## Book Builder - Technology selection

Selecting the correct technology is the first important technical decision on any project.
Book Builder is a web service that can support both desktop and mobile web clients.
The technology to be used should be optimized for rapid web development.

### Technology Alternatives

Existing Commercial Product 

Before starting any project it is important to understand the competitive landscape.  
Are there any commercial products available that could be used instead of building a new
software. Building software will be at least ten times more expensive that buying an
existing product.

There are some competitive products in the market but there is nothing that will satisfy 
the client needs.  We will be building software to create the Book Builder application.
It is important to the client to own the intellectual property so that the application can be
sold to another business.

Content Mangement System

The first solution to be considered is a CMS (Content Mangement System). Examples 
include WordPress, Joomla, and Drupal.  A CMS is built around the idea of publishing 
articles and an editorial workflow that is associated.

With very little customization a CMS can be configured to allow end-users to create and 
maintain their own content.  The difficulty is often trying to get the exact user experience
that will please the client.  Custom software is probably required in this case to meet the 
business goals.

Web Development Framework

There are several web development frameworks available that will all meet the project needs.
Strong consideration was given to the following frameworks.

* ASP.net - Microsoft web development 
* Ruby on Rails - Strong developer community
* Python with Django - Strong developer community, security, popularity
* Node with React and Mongo DB - Thriving community and very popular


### Select Development Tools

Criteria for Technology Selection

* Fitness of the tool for the job
* Experience of the development team with the technology
* Components that can be leverage from previous work
* Professional opinion and popularity
* Productivity benchmarks
* Security concerns
* Community of users and developers
* Existing commercial apps that use the technology
* Proof of concept (building a simple app)

After careful consideration a decision was made to create Book Builder using the Django
web framework which is written in the Python programming language.

Here are the most important considerations that support this decision:

* The software team has extensive experience with using Django for the past several 
years.  The accumulated Django experience of the team is 25 years.
* The new software is very similar to several existing products that have already been
completed, allowing for extensive leverage opportunities.
* Python is growing in popularity and widespread market adoption and Django is the most
popular web framework written in Python.  
* JavaScript is also a good choice (with Node, React, Mongo DB), but the dev team did not
have adequate experience and would need to climb a steep learning curve.
* Django provides first class solutions for Security, Object Relational Mapping, and 
View templates that create amazing productivity.


### Infrastructure - Frameworks & Tools

Framework

    Python 3.7.6
    Django 3.0.8
    Virtual Environment
    
Web hosting

    Python Anywhere
    
Dev Tools

    Pycharm Professional 2020.1  -- Each developer can choose their own tools
    Sublime Text 3.2
    Brackets 1.14
    
Github

    Git for version control
    Github to hold the Book Builder repos
        * Book-Builder.git - app code 
        * Book-Builder.github.io.git - Github Pages for client website
        * Book-Builder.wiki.git
    Github Tools
        * wiki - project documentation
        * kanban - project management workflow
        * issues - issue tracking system
        * gitter - instant messaging system
        
Python Anywhere

    Account:  markseaman
    Web URL:  https://markseaman.pythonanywhere.com
    

### Setup Guides

* [Tutorial Documents](../docs/Index.md)


### Create "Hello World"

* [Hello World](../docs/HelloWorld.md) - This simple app ensures that all of the development 
tools are installed and properly configured.  All developers will do this before any other 
work is done with the code.
* [Code Repo](https://github.com/Mark-Seaman/Book-Builder) - 
Source code is located in "test/hello" directory.


### Decide on App deployment

Alternative Hosting Services

* AWS - Powerful, high-priced, complex initial setup
* Heroku - Turn key solution for Django apps
* Digital Ocean - Simple yet powerful (Shrinking World uses this)
* Python Anywhere - Free accounts available, optimized for Django
* Bluehost - Supports PHP but not Django

Book Builder will be using Python Anywhere to do free hosting.  Tutorial documents will show
all developers how to setup and configure a web app.

