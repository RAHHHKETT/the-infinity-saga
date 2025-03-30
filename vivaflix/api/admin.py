from django.contrib import admin
from .models import Watchlist, Movie, Collection

admin.site.register(Watchlist)
admin.site.register(Movie)
admin.site.register(Collection)