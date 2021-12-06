
from django.urls import path
from . import views
app_name='dashboard'

urlpatterns = [
    path('home/',views.home,name="home"),
  #  path('home',views.HomepageViewCBV.as_view(),name="home"),
]
