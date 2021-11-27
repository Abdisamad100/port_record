from django.urls import path
from . import views
urlpatterns = [
   path("register", views.register_request, name="register"),
   path("", views.login_request, name="login"),
   path("homepage/", views.home, name="home")
]