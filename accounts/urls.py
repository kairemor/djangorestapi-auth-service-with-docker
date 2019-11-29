from django.urls import include, path
from knox import views as knox_views
from rest_framework import routers

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/users', UsersAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
]
