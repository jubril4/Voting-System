from django.urls import path
from . import views

urlpatterns = [
    path("", views.vote, name="home"),
    path("vote/", views.vote, name="vote"),
    path("results/", views.results, name="results"),
]
