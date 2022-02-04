from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('<int:pk>', views.MovieDetailView.as_view())
]
