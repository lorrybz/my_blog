
from django.urls import path

from app import views

urlpatterns = [
    path(r'index/', views.index, name='index'),
]
