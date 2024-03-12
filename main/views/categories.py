from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models.categories import Category
from main.serializers.categories import CategorySerializer


class CategoryListGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        return Category.objects.filter(parent__isnull=True)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryListByParentIDGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()

    def get(self, request, parent_id, *args, **kwargs):
        sub_categories = Category.objects.filter(parent_id=parent_id)
        serializer = self.get_serializer(sub_categories, many=True)
        return Response(serializer.data)


class SubCategoryListGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(parent__isnull=False)

    def get(self, request, *args, **kwargs):
        sub_categories = self.get_queryset()
        serializer = self.get_serializer(sub_categories, many=True)
        return Response(serializer.data)
