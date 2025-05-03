from django.urls import path
from . import views 
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(r'maps', views.MapViewSet)
router.register(r'markers', views.MarkerViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('signup/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('company/signup/', views.register_company, name='register_company'),
    path('company/login/', views.login_company, name='login_company'),

    
    path('api/', include(router.urls)),  
]