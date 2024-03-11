from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from main.models.telegram_users import TelegramUser
from main.serializers.telegram_users import TelegramUserSerializer


class AddTelegramUserGenericAPIView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self, *args, **kwargs):
        return TelegramUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
