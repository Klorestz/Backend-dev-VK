from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.chats_list, name='chats_list'),
    path('chats_list/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('create_chat/', views.create_chat, name = 'create_chat'),
    path('edit_chat/', views.edit_chat, name='edit_chat'),
    path('delete_chat/', views.delete_chat, name='delete_chat')
]