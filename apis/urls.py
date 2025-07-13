from django.urls import path

from . import views

urlpatterns = [
    # books app urls
    path("books/", views.BookAPIView.as_view(), name="book_list_api"),

    # todos app urls
    path("todos/", views.ListTodo.as_view(), name="todo_list_api"),
    path("todos/<int:pk>", views.DetailTodo.as_view(), name="todo_detail_api"),
]
