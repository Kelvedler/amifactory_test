from . import models
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.core import exceptions


def get_movie_dict(movie):
    return {'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'release_year': movie.release_year,
            'mpa_rating': movie.mpa_rating,
            'duration': movie.duration,
            'poster': movie.poster.url,
            'bg_picture': movie.bg_picture.url,
            'genres': list(movie.genres.values('id', 'title')),
            'directors': list(movie.directors.values('id', 'first_name', 'last_name')),
            'writers': list(movie.writers.values('id', 'first_name', 'last_name')),
            'stars': list(movie.stars.values('id', 'first_name', 'last_name'))}


class MovieListView(ListView):

    model = models.Movie

    def get(self, request, *args, **kwargs):
        query_parameters = request.GET
        query_filter = {}
        error_set = set()
        if query_parameters.get('genre'):
            try:
                query_filter['genres'] = int(query_parameters.getlist('genre')[0])
            except ValueError:
                error_set.add('genre__invalid')
        if query_parameters.get('src'):
            if len(query_parameters.get('src')) < 2 or len(query_parameters.get('src')) > 20:
                error_set.add('src__invalid')
            query_filter['title__startswith'] = query_parameters.get('src')
        if query_filter:
            movie_queryset = self.get_queryset().prefetch_related().filter(**query_filter)
            if 'genre__invalid' not in error_set and query_filter.get('genres') and not movie_queryset.filter(
                    genres=query_filter['genres']).exists():
                error_set.add('genre__invalid')
        else:
            movie_queryset = self.get_queryset().prefetch_related().all()
        paginated_movies = Paginator(movie_queryset, 20)
        total_pages = paginated_movies.num_pages
        if query_parameters.get('page'):
            try:
                page = int(query_parameters.get('page'))
            except ValueError:
                error_set.add('page__invalid')
            else:
                if total_pages < page:
                    error_set.add('page__out_of_bounds')
                else:
                    movies = paginated_movies.page(page)
        else:
            movies = paginated_movies.page(1)
            page = 1
        if error_set:
            return JsonResponse({'errors': list(error_set)}, status=400)
        else:
            movies = [get_movie_dict(movie) for movie in movies]
            return JsonResponse({'page': page, 'total': total_pages, 'results': movies})


class MovieDetailView(DetailView):

    model = models.Movie

    def get(self, request, pk=None, *args, **kwargs):
        try:
            movie = self.get_queryset().get(pk=pk)
            return JsonResponse(get_movie_dict(movie), safe=False)
        except exceptions.ObjectDoesNotExist:
            return JsonResponse({'error': 'movie__not_found'}, status=404)
