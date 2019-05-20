from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView,LogoutView

app_name = "Users"
urlpatterns = [
    path('',views.home,name="homepage" ),
    path('login/',views.login_request,name="login"),
    path('logout/',views.logout_request, name="logout"),
    path('signup/',views.signup,name="signup"),
]
