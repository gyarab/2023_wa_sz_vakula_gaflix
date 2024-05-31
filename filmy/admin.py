from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "footage", "genres_display", "director"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "director__name"]
    list_filter = ["genres", "year"]


class DirectorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)