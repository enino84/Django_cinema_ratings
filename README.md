# simple_cinema_ratings
This is a simple web-based system via Django for movie/film ratings.

To run this app, simply:

1. Clone this repo
2. Start the server: in the main folder, open a shell and type `python3 manage.py runserver`
3. By default, the web service will be hosted in `http://127.0.0.1:8000/` and the app can be accessed thru `http://127.0.0.1:8000/cinema`

Since this app is based on Django framwork, in this example, I consider three layers distributed in three files, each one with a responability:

1. `urls.py`: defines the navigation rules regarding GET and POST HTTP requests.
2. `views.py`: defines the actions to take regarding urls
3. `methods.py`: is an additional layer for handling communication with the persistence layer (database), this employs the `django.db` module.

In this manner, I don't mix code from the persistence layer with that from the views one, for example. Databases queries are encapsulated thru the `django.db` module so there are no explicit sql statements in this project.

The view define the following methods:
1. `def index(request)`: route requests to the index page.
2. `def register_owner(request)`: allows users to register. The following validations are performed prior any registration:
* Validate email is a valid email address.
* Validate email is not already registered in the database.
* Validate password contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ].
* If any of the above is not valid, send back a meaningful response.
3. `def main_menu(request)`:
4. `def register_movie_form(request)`:
5. `def register_movie_action(request)`:
6. `def list_of_movies(request)`:
7. `def delete_movie_action(request, movie_id)`:
8. `def update_movie_action(request, movie_id, publicp)`:
9. `def restart_database(request)`<:

    
    
    



