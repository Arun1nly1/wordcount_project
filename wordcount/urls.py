from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('countword/',views.count,name="count"),


]
