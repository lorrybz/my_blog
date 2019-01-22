from django.urls import path
from front import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('infopic/<int:id>/',views.infopic,name='infopic'),
    path('list/',views.list,name='list'),
]