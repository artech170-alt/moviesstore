from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('create/', views.create, name='petitions.create'),
    path('vote/<int:petition_id>/', views.vote, name='petitions.vote'),
]