from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('<str:room_id>/vote', views.vote, name='vote'),
    path('<str:room_id>/results', views.results, name='results'),
]