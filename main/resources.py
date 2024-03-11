from import_export import resources

from main.models.categories import Category
from main.models.films import Film
from main.models.telegram_users import TelegramUser


class TelegramUserResource(resources.ModelResource):
    class Meta:
        model = TelegramUser


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class FilmResource(resources.ModelResource):
    class Meta:
        model = Film
