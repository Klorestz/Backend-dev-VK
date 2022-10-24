from django.urls import path

from . import views

urlpatterns = [
    path('', views.chats_list, name='chats_list'),
    path('<int:chat_id>/', views.page_of_chat, name='page_of_chat'),
    path('create_chat/', views.create_chat, name = 'create_chat')
]