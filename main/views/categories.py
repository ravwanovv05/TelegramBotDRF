from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models.categories import Category
from main.serializers.categories import CategorySerializer


class CategoryListGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
