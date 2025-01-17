# Movie Web Application
##Introduction

This web can be used to browser movies by using keywords( title, actor, genre, director and year).

##Features

1. Browsing movies
2. Searching for movies by actor, genre and director
3. Registering, logging in and logging out users
4. Making comments after logging in


## Description

A Web application that demonstrates use of Python's Flask framework. The application makes use of libraries such as the Jinja templating library and WTForms. Architectural design patterns and principles including Repository, Dependency Inversion and Single Responsibility have been used to design the application. The application uses Flask Blueprints to maintain a separation of concerns between application functions. Testing includes unit and end-to-end testing using the pytest tool.

## Installation

**Installation via requirements.txt**

```shell
$ cd COMPSCI-235\ 2
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI-235 2' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment.

## Execution

**Running the application**

From the *COMPSCI-235 2* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
````


## Configuration

The *COMPSCI-235 2/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.


## Testing

Testing requires that file *COMPSCI-235 2/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *COMPSCI-235 2/tests/data* directory.

E.g.

`TEST_DATA_PATH = os.path.join('Macintosh HD', os.sep, 'Users', 'alina', 'Desktop', 'COMPSCI-235 2', 'data')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):

`'Macintosh HD', os.sep, 'Users', 'alina', 'Desktop', 'COMPSCI-235 2', 'data'`

You can then run tests from within PyCharm.
