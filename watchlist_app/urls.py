from django.urls import path
from watchlist_app import views

urlpatterns = [
    path('list/', views.movie_list, name= 'movie-list'),
    path('<int:pk>', views.movie_details, name= 'movie-details') # if there is any integer, it is gonna be send to the view as pk
]
