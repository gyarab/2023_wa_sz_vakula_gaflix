from django.contrib import admin
from filmy.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelMovie):
    pass

admin.site.Register(Movie, MovieAdmin)