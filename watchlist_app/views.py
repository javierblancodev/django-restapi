from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    # Create a query set: select some/all objects available in our database for a model
    movies = Movie.objects.all() # return a querySet
    movies_list = list(movies.values()) # .values convert the model instances into dictionaries, when is used as iterable
    
    data = {
        "movies": movies_list
    }
    
    # These dictionaries has model field name as key and  model field value as a value, so we can use it as a response with JsonResponse
    return JsonResponse(data)
    
    
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk) # Recall that these objects/instances will return its name property as states the str method in the model
    
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    
    return JsonResponse(data)