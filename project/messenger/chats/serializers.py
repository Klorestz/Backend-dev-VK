from rest_framework import serializers
from chats.models import Chat, Message, ChatMember

class ChatListSerializer(serializers.ModelSerializer):
    chat = serializers.CharField(source='get_info_chat')

    class Meta:
        model = ChatMember
        fields = ['chat']

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

class ChatMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMember
        fields = '__all__'