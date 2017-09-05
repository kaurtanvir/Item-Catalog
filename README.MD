# Item Catalog
This application is a catalog of items within a variety of categories with a brief description of the items.

## Features
1.	It is a RESTful web application using the Python framework Flask.
2.  It implements a third-party oauth implementation using google and facebook.
3.  It provides a user registration and authentication system in which the        registered user have the ability to post, edit and delete their own items.
	  
    
## Installation
1.	Install Vagrant and VirtualBox
2.  Clone the repo.
3.  Launch the Vagrant VM(using vagrant up).
4.	Make sure python as well as python modules(sqlalchemy) and db sqllite is installed on the virtual machine.
5.	Run 'python database_setup.py' to create the db required for the application to run.
6.	Run 'python database_populator.py' to create the tables required for the application.
7.	Run 'python project.py' to get the localhost up and running on port :5000.
8.	Go to url 'localhost:5000' to view the page.



