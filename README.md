# LAB - Class 31

## Project: Django REST Framework & Docker

## Author: Jason Christopher

### Description

* Django app that allows users to input homes with the following attributes: (owner, street address, city, state, square feet, and description). The site acts like an API and returns JSON data when queried.

### Setup

1. Copy repo and clone down to local machine.
2. Create and activate virtual environment.
3. Run `pip install -r requirements.txt`
4. Run `python manage.py makemigrations` and `python manage.py migrate`.
5. Run `python manage.py runserver` and copy the localhost URL with `/admin` at the end.
6. Log-in to the Django admin portal with the username "***admin***" and password "***12345***".
7. Add, delete, or modify a home entry.
8. Run `docker-compose up` to create a Docker container (not sure if that's the correct terminology).

### Tests

* Run tests with the command: `python manage.py test`.
* It fails 2 of the tests, but I don't know why.
