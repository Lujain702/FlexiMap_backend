from django.contrib import admin
from .models import Map, Marker, Comment, Category, Tag

admin.site.register(Map)
admin.site.register(Marker)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)


# Register your models here.
