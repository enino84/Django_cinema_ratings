from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.index, name='logout'),
    path('register_owner', views.register_owner, name='register_owner'),
    path('main_menu', views.main_menu, name='main_menu'),
    path('register_movie_form', views.register_movie_form, name='register_movie_form'),
    path('register_movie_action', views.register_movie_action, name='register_movie_action'),
    path('list_of_movies', views.list_of_movies, name='list_of_movies'),
    path('delete_movie_action/<int:movie_id>/', views.delete_movie_action, name='delete_movie_action'),
    path('update_movie_action/<int:movie_id>/<int:publicp>/', views.update_movie_action, name='update_movie_action'),
    path('restart_database', views.restart_database, name='restart_database'),
]
