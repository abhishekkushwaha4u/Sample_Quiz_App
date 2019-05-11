from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.home ),
    path('login/',LoginView.as_view(template_name="Users/login.html")),
    path('logout/',LogoutView.as_view(template_name="Users/logout.html")),
]