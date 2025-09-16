from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = Movie.objects.get(pk=obj.pk)
            # Prevent changing stock if it is already 0
            if old_obj.stock == 0 and obj.stock != 0:
                return  # Do not save changes if trying to increase stock from 0
        super().save_model(request, obj, form, change)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)


# Register your models here.
