from django.urls import path
from main.views.films import (
    AddFilmGenericAPIView, SearchFilmListAPIView, FilmListGenericAPIView,
    FilmsByCategoryGenericAPIView, FilmDetailGenericAPIView, UpdateFilmMessageIdGenericAPIView)
from main.views.telegram_users import AddTelegramUserGenericAPIView, TelegramUserListGenericAPIView
from main.views.categories import (
    CategoryListGenericAPIView, SubCategoryListByParentIDGenericAPIView,
    SubCategoryListGenericAPIView)

urlpatterns = [
    # user
    path('add-user', AddTelegramUserGenericAPIView.as_view(), name='add_user'),
    path('telegram-user-list', TelegramUserListGenericAPIView.as_view(), name='telegram_user_list'),

    # category
    path('category-list', CategoryListGenericAPIView.as_view(), name='category_list'),
    path('sub-categories/<int:parent_id>', SubCategoryListByParentIDGenericAPIView.as_view(), name='sub_categories'),
    path('sub-categories-list', SubCategoryListGenericAPIView.as_view(), name='sub_categories_list'),

    # film
    path('add-film', AddFilmGenericAPIView.as_view(), name='add_film'),
    path('search-film', SearchFilmListAPIView.as_view(), name='search_film'),
    path('film-list', FilmListGenericAPIView.as_view(), name='film_list'),
    path('films-by-category/<int:category>', FilmsByCategoryGenericAPIView.as_view(), name='films_by_category'),
    path('film-detail/<int:film_id>', FilmDetailGenericAPIView.as_view(), name='film_detail'),
    path('update-film/<file_unique_id>', UpdateFilmMessageIdGenericAPIView.as_view(), name='update_film_message_id'),
]
