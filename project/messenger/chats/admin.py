from django.contrib import admin
from  chats.models import Chat, Message


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_filter = ('title',)
    search_fields = ('title',)
    autocomplete_fields = ('users',)
    raw_id_fields = ["users"]



class MessageAdmin(admin.ModelAdmin):
    list_display = ( 'chat', 'content', 'sender', 'send_date')
    list_filter = ('chat', 'content')
    search_fields = ('chat', 'content')
    autocomplete_fields = ('sender', 'chat')
    raw_id_fields = ["sender", 'chat']
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
# Register your models here.
