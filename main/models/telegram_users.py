from django.db import models


class TelegramUser(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Last name')
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name='Username')
    telegram_id = models.CharField(max_length=100, unique=True, verbose_name='Telegram ID')
    language = models.CharField(max_length=5, verbose_name='Language')
    join_at = models.DateTimeField(auto_now_add=True, verbose_name='Join at')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
