from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from main.models.films import Film
from main.serializers.films import FilmSerializer


class AddFilmGenericAPIView(GenericAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Film.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SearchFilmListAPIView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class FilmListGenericAPIView(GenericAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Film.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Film.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FilmsByCategoryGenericAPIView(GenericAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self, *args, **kwargs):
        return Film.objects.all()

    def get(self, request, category, *args, **kwargs):
        films = Film.objects.filter(category=category)
        serializer = self.get_serializer(films, many=True)
        return Response(serializer.data)


class FilmDetailGenericAPIView(GenericAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self, *args, **kwargs):
        return Film.objects.all()

    def get(self, request, film_id, *args, **kwargs):
        film = Film.objects.get(id=film_id)
        serializer = self.get_serializer(film)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateFilmMessageIdGenericAPIView(GenericAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self, *args, **kwargs):
        return Film.objects.all()

    def patch(self, request, file_unique_id):
        film = Film.objects.filter(file_unique_id=file_unique_id).first()
        serializer = self.get_serializer(film, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
