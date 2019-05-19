from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = "Users"
urlpatterns = [
    path('',views.home,name="homepage" ),
    path('login/',LoginView.as_view(template_name="Users/login.html"),name="login"),
    path('logout/', LogoutView.as_view(template_name="Users/logout.html"), name="logout"),
    path('signup/',views.signup,name="signup"),
]
