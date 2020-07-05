from . import views
from django.urls import path
urlpatterns=[
    path('',views.Home,name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.chatting, name='showchat'),
]