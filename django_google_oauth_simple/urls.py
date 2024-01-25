from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
]
