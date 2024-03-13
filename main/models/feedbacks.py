from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name')
    telegram_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='Telegram ID')
    message = models.TextField(blank=True, null=True, verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.name
