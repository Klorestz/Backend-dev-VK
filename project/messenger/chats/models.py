from django.db import models
from users.models import User
#chat_member добавить
class Chat(models.Model):
    title = models.CharField('Наименование чата', max_length=200, blank=True, null=True)
    description = models.TextField('Описание чата', blank=True, null=True)
    users = models.ManyToManyField(
        User,
        related_name='user_chats',
        verbose_name = 'Пользователи чата',
    )
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
    send_date = models.DateField('Время отправления')
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
