from django.urls import path, include
from .views import auth_view, home, custom_logout

urlpatterns = [ 
    path("", view=home, name="home"),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
    path("signup/", view=auth_view, name='signup'),
    path('logout/', view=custom_logout, name='logout'),
]
