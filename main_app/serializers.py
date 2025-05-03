from rest_framework import serializers
from .models import Map
from .models import Marker
from .models import Map, Marker, Category, Comment, Tag


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['id', 'name', 'description', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
