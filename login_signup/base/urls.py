from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import auth_view, home, custom_logout

urlpatterns = [ 
    path("", view=home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", view=auth_view, name="auth_view"),
    path('logout/', view=custom_logout, name='logout'),
]
