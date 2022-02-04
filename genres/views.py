from . import models
from django.http import JsonResponse
from django.views.generic import ListView


class GenreListView(ListView):

    model = models.Genre

    def get(self, request, *args, **kwargs):
        genres = list(self.get_queryset().values('id', 'title'))
        return JsonResponse(genres, safe=False)
