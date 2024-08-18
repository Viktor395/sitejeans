
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('man', views.man),
    path('woman', views.woman),
]
