from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from .serializers import MarkerSerializer
from rest_framework import viewsets
from .models import Map, Marker, Category, Comment, Tag
from .serializers import MapSerializer, MarkerSerializer, CategorySerializer, CommentSerializer, TagSerializer

User = get_user_model()

# -------------------

@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create_user(
            email=data['email'],
            password=data['password']
        )
        return Response({'message': 'User registered successfully'})
    except Exception as e:
        return Response({'error': f'Registration failed: {str(e)}'}, status=400)

# -------------------

@api_view(['POST'])
def login_user(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    user = authenticate(request, email=email, password=password)
    if user:
        return Response({'message': 'Login successful'})
    return Response({'error': 'Invalid credentials'}, status=400)

# -------------------

@api_view(['POST'])
def register_company(request):
    data = request.data
    try:
        company = User.objects.create_user(
            email=data['email'],
            password=data['password'],
            is_company=True,
            company_name=data.get('company_name', '')
        )
        return Response({'message': 'Company registered successfully'})
    except Exception as e:
        return Response({'error': f'Registration failed: {str(e)}'}, status=400)

# -------------------

@api_view(['POST'])
def login_company(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    user = authenticate(request, email=email, password=password)
    if user and user.is_company:
        return Response({'message': 'Company login successful'})
    return Response({'error': 'Invalid credentials'}, status=400)

# -------------------

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
