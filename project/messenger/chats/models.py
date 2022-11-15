from django.db import models
from users.models import User
class Chat(models.Model):
    title = models.CharField('Наименование чата', max_length=200, blank=True, null=True)
    description = models.TextField('Описание чата', blank=True, null=True)
    created_at = models.DateField('Время создания', auto_now_add=True)
    photo = models.ImageField('Аватар чата', null=True, blank=True)
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
class Message(models.Model):
    content = models.TextField('Текст сообщения')
    sender = models.ForeignKey(
        User,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'sender_message',
        verbose_name = 'Отправитель',
    )
    send_date = models.DateField('Время отправления', auto_now_add=True)
    chat = models.ForeignKey(
        Chat,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'chat_messages',
        verbose_name = 'Чат',
    )
    is_readen = models.BooleanField('Прочиатно', default=False, null=True, blank=True)
    def __str__(self):
        return f'{self.content} {self.sender}'
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        verbose_name = 'Чат',
        related_name = 'chat_chatmembers',
        on_delete=models.SET_NULL,
        null = True,
    )
    user = models.ForeignKey(
        User,
        verbose_name = 'Пользователь',
        related_name = 'user_chatmembers',
        on_delete = models.SET_NULL,
        null = True,
    )
    role = models.CharField('Роль пользователя',max_length=200, null=True, blank=True)
    member_since = models.DateField('Время вступления в чат', auto_now_add=True)
    def __str__(self):
        return f'{self.chat} {self.user}'
    class Meta:
        verbose_name = 'Пользователь чата'
        verbose_name_plural = 'Пользователи чата'