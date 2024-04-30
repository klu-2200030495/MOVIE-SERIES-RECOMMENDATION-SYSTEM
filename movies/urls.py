# urls.py
from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path("test/", views.test, name='test'),
    path("privacypolicy/", views.privacypolicy, name='privacypolicy'),
    # path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path("login/movies/", views.movie_list, name='movie_list'),
]
