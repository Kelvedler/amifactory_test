from django.db import models
from genres import models as genres_models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


class Person(models.Model):

    class Types(models.TextChoices):
        DIRECTOR = 'director', _('director')
        WRITER = 'writer', _('writer')
        ACTOR = 'actor', _('actor')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    types = MultiSelectField(max_length=8, choices=Types.choices, max_choices=3)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):

    class MpaRating(models.TextChoices):
        G = 'G', _('G')
        PG = 'PG', _('PG')
        PG13 = 'PG-13', _('PG-13')
        R = 'R', _('R')
        NC17 = 'NC-17', _('NC-17')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    poster = models.FileField(upload_to='poster/')
    bg_picture = models.FileField(upload_to='bg_picture/')
    release_year = models.PositiveSmallIntegerField()
    mpa_rating = models.CharField(max_length=5, choices=MpaRating.choices)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2)
    duration = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField(genres_models.Genre)
    directors = models.ManyToManyField(Person, related_name='directors')
    writers = models.ManyToManyField(Person, related_name='writers')
    stars = models.ManyToManyField(Person, related_name='stars')

    def __str__(self):
        return f'{self.title}, {self.release_year}'

