from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.profile),
    path("login/series/", views.series_list, name='series_list'),
    path("reset/",views.reset)
]