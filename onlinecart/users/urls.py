
from django.urls import path
from . import views
app_name="users"
urlpatterns = [
    path('login/',views.Login,name="login"),
    path('logout/', views.LogOut, name="logout"),
    path('signup/', views.SignUp, name="signup"),
    path('authenticate/', views.Authenticate, name="authenticate"),
]
