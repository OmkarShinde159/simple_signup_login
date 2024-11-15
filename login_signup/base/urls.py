from django.urls import include, path

from .views import auth_view, custom_logout, home

urlpatterns = [
    path("", view=home, name="home"),
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),
    path("signup/", view=auth_view, name="signup"),
    path("logout/", view=custom_logout, name="logout"),
]
