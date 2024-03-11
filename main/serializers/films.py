from rest_framework.serializers import ModelSerializer, IntegerField
from main.models.films import Film


class FilmSerializer(ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'


class PagedFilmSerializer(ModelSerializer):
    from_ = IntegerField()
    to_ = IntegerField()

    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = '__all__'

