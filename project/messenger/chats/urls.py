from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.chats_list, name='chats_list'),
    path('chats_list/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('create_chat/', views.create_chat, name = 'create_chat'),
    path('edit_chat/', views.edit_chat, name='edit_chat'),
    path('delete_chat/', views.delete_chat, name='delete_chat'),
    path('add_member/', views.add_member, name='add_member'),
    path('delete_member/', views.delete_member, name='delete_member'),
    path('create_message/', views.create_message, name='create_message'),
    path('edit_message/', views.edit_message, name='edit_message'),
    path('readen_message/', views.message_is_readen, name='message_is_readen'),
    path('delete_message/', views.delete_message, name='delete_message'),
    path('list_of_message/', views.list_of_messages, name='list_of_message'),
]