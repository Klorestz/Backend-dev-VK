# Generated by Django 4.1.2 on 2022-11-07 20:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_alter_message_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(related_name='users_chat', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи чата'),
        ),
    ]
