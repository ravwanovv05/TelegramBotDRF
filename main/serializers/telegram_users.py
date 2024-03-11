from rest_framework.serializers import ModelSerializer, ValidationError
from main.models.telegram_users import TelegramUser


class TelegramUserSerializer(ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = '__all__'

    def validate(self, attrs):
        telegram_id = attrs['telegram_id']
        if TelegramUser.objects.filter(telegram_id=telegram_id).exists():
            raise ValidationError("This Telegram User already exist.")
        return attrs

