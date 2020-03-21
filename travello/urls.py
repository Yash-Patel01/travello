from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destinations', views.destinations, name='destinations'),
    path('destinations1', views.destinations1, name='destinations1'),
    path('register1', views.register1, name='register1'),
]