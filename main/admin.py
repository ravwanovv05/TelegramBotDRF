from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from main.models import Feedback
from main.models.categories import Category
from main.models.films import Film
from main.models.telegram_users import TelegramUser
from main.resources import TelegramUserResource, FilmResource, CategoryResource


@admin.register(TelegramUser)
class TelegramUserAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'language', 'telegram_id', 'join_at')
    list_display_links = ('first_name',)
    search_fields = ('first_name',)
    list_per_page = 10
    resource_class = TelegramUserResource


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10
    resource_class = CategoryResource


@admin.register(Film)
class FilmAdmin(ImportExportModelAdmin):
    list_display = ('name', 'release_date')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10
    resource_class = FilmResource


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'telegram_id', 'created_at')
