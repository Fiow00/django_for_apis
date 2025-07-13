from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BookAPIView.as_view(), name="book_list_api"),
]
