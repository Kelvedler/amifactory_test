from django.contrib import admin
from . import models


class MovieAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Person, PersonAdmin)
