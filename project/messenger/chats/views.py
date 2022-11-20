from chats.models import Chat, Message, ChatMember
from users.models import User
from chats.serializers import *
from rest_framework.generics import *
from rest_framework.filters import BaseFilterBackend

class ChatList(ListAPIView):
    # Получение списка чатов по id пользователя
    serializer_class = ChatListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return ChatMember.objects.filter(user=user_id)

class ChatListCreate(ListCreateAPIView):
    #Список всех чатов проекта и создание новых
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

class ChatEditDeleteUpdate(RetrieveUpdateDestroyAPIView):
    #Редактирование, удаление конкретного чата по id
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    lookup_field = 'id'

class MessageListCreate(ListCreateAPIView):
    #Получение сообшений конкретного чата и создание новых
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat=chat_id)

class MessageEditDeleteUpdate(RetrieveUpdateDestroyAPIView):
    #Редактирование сообщения по id
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'

class ChatMemberDelete(RetrieveDestroyAPIView):
    #Удаление пользователя из чата по id пользователя и id чата
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()
    multiple_lookup_fields = ['chat', 'user']

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

class ChatMemberCreateList(ListCreateAPIView):
    #Добавление пользователя в чат
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()