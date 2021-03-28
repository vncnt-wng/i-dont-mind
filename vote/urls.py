from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_room_id', views.get_room_id, name='get_room_id'),
    path('<str:room_id>/create_question', views.create_question, name='create_question'),
    path('<str:room_id>/create_choices', views.create_choices, name='create_choices'),
    path('<str:room_id>/vote', views.vote, name='vote'),
    path('<str:room_id>/results', views.results, name='results'),
    path('about', views.about, name='about')
]