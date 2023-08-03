from django.contrib import admin
from .models.contact import Contact
from .models.gallary import Gallary
from .models.movie import Movie
from .models.about import About


# Register your models here.

admin.site.register(Contact)
admin.site.register(Gallary)
admin.site.register(Movie)
admin.site.register(About)

