# Flask Boilerplate
A skeleton of decent Flask app.

## Features
- [X] Procfile-based
- [X] Redis
- [x] SQLAlchemy
- [x] RQ
- [x] Mail

## Directory Layout

    .
    ├── Procfile                      # Procfile-based
    ├── app                           # Core application code, including models, views, templates, etc..
    │   ├── __init__.py               # Where app instance created, extenstions initialized
    │   ├── mailers                   # Mailers workers
    |   ├── models                    # Models files
    |   ├── static                    # Static files accessible to the public
    │   └── templates                 # Template files
    ├── config.py                     # Application configuration
    ├── db                            # Database files
    ├── manage.py                     # Launches the application
    ├── migrations                    # Database migration scripts
    ├── requirements.txt              # Package dependences
    └── tests                         # Application tests


## Getting Started

1. Git clone repository

    ```
    git clone https://github.com/hbin/flask-boilerplate.git && cd flask-boilerplate
    ```

2. Create venv

    ```
    virtualenv venv && source venv/bin/activate
    ```

3. Install packages from reqirements.txt

    ```
    pip install -r requirements.txt
    ```

4. Edit .env file
    ```
    cp .env.example .env
    ```

5. Run server

   Perfer to use [Foreman](https://github.com/ddollar/foreman). There is also a python port - [Honcho](https://github.com/nickstenning/honcho)

    ```
    foreman start   # or `honcho start`
    ```
  Or

    `python manage.py runserver`

6. Open `http://localhost:5000/`


### Tips:
* If you mind the git commit history, feel free to rm .git folder, and then git init.
