from django.urls import path

from . import views

urlpatterns = [
    # books app urls
    path("books/", views.BookAPIView.as_view(), name="book_list_api"),

    # todos app urls
    path("todos/", views.ListTodo.as_view(), name="todo_list_api"),
    path("todos/<int:pk>", views.DetailTodo.as_view(), name="todo_detail_api"),

    # blog app urls
    path("posts/", views.PostList.as_view(), name="post_list_api"),
    path("posts/<int:pk>/", views.PostDetail.as_view(), name="post_detail_api"),
]
