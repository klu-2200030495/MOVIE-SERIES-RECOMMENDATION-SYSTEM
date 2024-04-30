from django.shortcuts import render
from tmdbv3api import TMDb, Movie


# Create your views here.
def profile(request):
    return render(request, 'profile.html')


def reset(request):
    return render(request, 'resetpassword.html')


def series_list(request):
    # Initialize TMDB API
    tmdb = TMDb()
    tmdb.api_key = '60d3d7a3955eb7168386c2ae16fc5df1'  # Replace 'YOUR_API_KEY' with your actual API key

    # Retrieve popular movies
    movie_api = Movie()
    popular_movies = movie_api.popular()

    # Fetch additional details for each movie
    for movie in popular_movies:
        # Fetch cast information
        credits = movie_api.credits(movie.id)
        cast_list = []
        for actor in credits['cast']:
            cast_list.append(actor)
            if len(cast_list) >= 5:
                break
        movie.cast = cast_list
    # Fetch poster URLs for each movie
    for movie in popular_movies:
        movie_details = movie_api.details(movie.id)
        poster_path = movie_details.poster_path
        if poster_path:
            movie.poster_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            # If poster path is not available, use a default image URL or handle it as per your requirement
            movie.poster_path = "https://example.com/default-poster.jpg"

    context = {
        'movies': popular_movies,
    }
    return render(request, 'series_list.html', context)
