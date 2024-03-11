from rest_framework.serializers import ModelSerializer
from main.models.categories import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
