# simple_cinema_ratings
This is a simple system based on Django for movie/film ratings.

To run this app, simply:

1. Clone this repo
2. Start the server: in the main folder, open a shell and `type python3 manage.py runserver`
3. By default, the web service will be hosted in `http://127.0.0.1:8000/`

This app is based on Django framwork. In this example, we can think in three layers

1. `urls`: defines the navigation rules regarding GET and POST HTTP requests.
2. `views`: defines the actions to take regarding urls
3. `methods`: is an additional layer for handling communication with the persistence layer (database), this employs the `django.db` module.

Databases are encapsulated thru the `django.db` so there are no explicit sql statements in this project.

The view define the following methods:


