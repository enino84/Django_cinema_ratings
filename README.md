# simple_cinema_ratings
This is a simple web-based system via Django for movie/film ratings.

I suppose that `python3` and `Django` are available in your machine and properly configured (standard configuration).

To run this app, simply:

1. Clone this repo
2. Start the server: in the main folder, open a shell and type `python3 manage.py runserver`
3. By default, the web service will be hosted in `http://127.0.0.1:8000/` and the app can be accessed thru `http://127.0.0.1:8000/cinema`

Since this app is based on Django framwork, in this example, I consider three layers distributed in three files, each one with a responability:

1. `urls.py`: defines the navigation rules regarding GET and POST HTTP requests.
2. `views.py`: defines the actions to take regarding urls
3. `methods.py`: is an additional layer for handling communication with the persistence layer (database), this employs the `django.db` module.

In this manner, I don't mix code from the persistence layer (database access) with that from the views one, for example. Databases queries are encapsulated thru the `django.db` into the `methods.py` module so there are no explicit sql statements in this project. A `template` folder is provided as templates of dynamical websites. Across all methods, the `session` object is employed to handle sessions, and to check whether the session is active or not.`

The view define the following methods:
1. `def index(request)`: route requests to the index page.
2. `def register_owner(request)`: allows users to register. The following validations are performed prior to any registration:
* Validate email is a valid email address.
* Validate email is not already registered in the database.
* Validate password contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ].
* If any of the above is not valid, send back a meaningful response.
3. `def main_menu(request)`: this method validates whether a valid user tries to access the system. This is done by satisfying the following requirements:
* Validate email and password matches for a previous registered user.
* If any of the above is not valid send back a meaningful response.
* If all of the above are valid send back a payload including some way for users to identify themselves for subsequent requests. That way to identify users should be invalid after 20 minutes and the user must login again to continue communication with the server. This is done by setting the  session expiration as follows: `request.session.set_expiry(1200)` (1200 seconds). At each request, the system validates whether the session is still valid. You can change this parameter value at your convenience.
4. `def register_movie_form(request)`: routes the request towards `cinema/register_movie_form.html`.
5. `def register_movie_action(request)`: register a movie in the database.
6. `def list_of_movies(request)`: employs the template `cinema/list_of_movies.html` to show all movies with the following constraints:
* Users should be able to read all public elements in the table/collection.
* Users should be able to read all elements created by themselves.
* Users should be able to edit at least one field in one of their private items. In this context, users can update the scope of their item from `public` to `private`. Here, I employ a `select` element from HTML.
* Validate that users are trying to read or update their private elements, otherwise send a meaningful response. To acomplish this, the private list is separated from the public one. The private one can be edited while the public one not.
8. `def delete_movie_action(request, movie_id)`: this deletes a given movie_id.
9. `def update_movie_action(request, movie_id, publicp)`: this updates the scope of a movie item from public to private or vice versa.
10. `def restart_database(request)`: this function is for testing purposes; this restarts the database (delete all entries) and creates some dummy records.

The methods from the `view.py` methods in the `methods.py` file as follows:

| views.py/methods.py     	| `is_valid_password` 	| `is_valid_email` 	| `register_user` 	| `validate_user` 	| `validate_login` 	| `register_movie` 	| `get_public_movies` 	| `get_owned_movies` 	| `delete_movie` 	| `update_movie` 	|
|-------------------------	|---------------------	|------------------	|-----------------	|-----------------	|------------------	|------------------	|---------------------	|--------------------	|----------------	|----------------	|
| `register_owner`        	| :blush:             	| :blush:          	| :blush:         	| :blush:         	|                  	|                  	|                     	|                    	|                	|                	|
| `main_menu`             	|                     	|                  	|                 	|                 	| :blush:          	|                  	|                     	|                    	|                	|                	|
| `register_movie_action` 	|                     	|                  	|                 	|                 	|                  	| :blush:          	|                     	|                    	|                	|                	|
| `list_of_movies`        	|                     	|                  	|                 	|                 	|                  	|                  	| :blush:             	| :blush:            	|                	|                	|
| `delete_movie_action`   	|                     	|                  	|                 	|                 	|                  	|                  	|                     	|                    	| :blush:        	|                	|
| `update_movie_action`   	|                     	|                  	|                 	|                 	|                  	|                  	|                     	|                    	|                	| :blush:        	|

Additionally, the program consider:

1. A git repository with the code and a README.md explaining how to run the code in the reviewer computer with very clear steps (this one).
2. Create the models for the selected topic with at least 5 meaningful fields.
3. Prefill the public elements with a list you built previously. *you can do this by choosing the option `Click here to populate/restart database` in the main site*.
4. Read requests must support pagination.
