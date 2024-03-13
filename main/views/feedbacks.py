from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Feedback
from main.serializers.feedbacks import FeedbackSerializer
from rest_framework import status


class FeedbackGenericAPIView(GenericAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self, *args, **kwargs):
        return Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
