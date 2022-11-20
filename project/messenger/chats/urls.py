from django.urls import path

from chats.views import *

urlpatterns = [
    path('chats_list/<int:user_id>/', ChatList.as_view(), name='chats_list'),
    path('chats_detail/<int:id>/', ChatEditDeleteUpdate.as_view(), name='chat_detail'),
    path('create_chat/', ChatListCreate.as_view(), name = 'create_chat'),
    path('messages_list/<int:chat_id>/', MessageListCreate.as_view(), name='create_message'),
    path('edit_message/<int:id>/', MessageEditDeleteUpdate.as_view(), name='edit_message'),
    path('add_member/', ChatMemberCreateList.as_view(), name='add_member'),
    path('delete_member/<int:chat>/<int:user>/', ChatMemberDelete.as_view(), name='delete_member'),
]