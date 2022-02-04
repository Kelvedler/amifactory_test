from django.contrib import admin
from . import models


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Genre, GenreAdmin)