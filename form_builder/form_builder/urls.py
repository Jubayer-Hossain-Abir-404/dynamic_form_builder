from django.contrib import admin
from django.urls import path

from base_app.views import (
    create_author,
    create_author,
    create_author_form,
    detail_author,
    create_book,
    create_book_form,
    detail_book,
    update_book,
    delete_book,
    create_book_form_number
)
# from form_builder.base_app.views import delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_author, name="create-author"),
    path('htmx/author-form/', create_author_form, name="author-form"),
    path('htmx/author-form/<pk>/', detail_author, name="detail-author"),
    path('htmx/book-form/', create_book_form, name="book-form"),
    path('htmx/book-form_num/', create_book_form_number, name="book-form-number"),
    path('htmx/book-form/<pk>/', detail_book, name="detail-book"),
    path('htmx/book-form/<pk>/update/', update_book, name="update-book"),
    path('htmx/book-form/<pk>/delete/', delete_book, name="delete-book"),
    path('<pk>/', create_book, name="create-book")
]
