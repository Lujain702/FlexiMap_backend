from django.db import models
from django.conf import settings  
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Map(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    tags = models.ManyToManyField('Tag', related_name='maps', blank=True)

    def save(self, *args, **kwargs):
        if not self.created_by:
            self.created_by = get_user_model().objects.first()  
        super(Map, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Marker(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='markers')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='markers', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')  # استبدال auth.User بـ settings.AUTH_USER_MODEL
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"Comment by {self.user} on {self.marker.name}"
