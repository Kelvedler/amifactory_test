from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreListView.as_view())
]
