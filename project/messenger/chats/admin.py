from django.contrib import admin
from  chats.models import Chat, Message, ChatMember
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_filter = ('title',)
    search_fields = ('title',)
class MessageAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'chat', 'content', 'sender', 'send_date', 'is_readen')
    list_filter = ('chat', 'content')
    search_fields = ('chat', 'content')
    autocomplete_fields = ('sender', 'chat')
    raw_id_fields = ["sender", 'chat']
class ChatMemberAdmin(admin.ModelAdmin):
    list_display = ( 'chat', 'user', 'role')
    list_filter = ('chat', 'user')
    autocomplete_fields = ('chat', 'user')
    raw_id_fields = ('chat', 'user')
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ChatMember, ChatMemberAdmin)

