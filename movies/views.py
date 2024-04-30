from django.http import HttpResponse
from tmdbv3api import TMDb, Movie
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or dashboard
                return redirect('movie_list')  # Change 'dashboard' to the appropriate URL name
            else:
                # Handle invalid login credentials
                error_message = "Invalid username or password."
    else:
        form = LoginForm()
        error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def navbar(request):
    return render(request, 'navbar.html')

def test(request):
    return render(request,'test.html')

def home(request):
    return render(request,'home.html')

def movie_list(request):
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
    return render(request, 'movie_list.html', context)
def privacypolicy(request):
    return render(request,'privacypolicy.html')
