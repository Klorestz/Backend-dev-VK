from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField('Никнейм', max_length=200, unique=True)
    first_name = models.CharField('Имя',max_length=200, null=True)
    last_name = models.CharField('Фамилия', max_length=200, null=True)
    bio = models.TextField('Биография', max_length=500, blank=True)
    location = models.CharField('Город', max_length=30, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    is_online = models.BooleanField('Статус', null=True, blank=True)
    last_visited = models.DateField('Последний визит', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
