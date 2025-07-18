from django.urls import path

from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users", views.UserViewSet, basename="users")
router.register("posts", views.PostViewSet, basename="posts")

urlpatterns = [
    # books app urls
    path("books/", views.BookAPIView.as_view(), name="book_list_api"),

    # todos app urls
    path("todos/", views.ListTodo.as_view(), name="todo_list_api"),
    path("todos/<int:pk>", views.DetailTodo.as_view(), name="todo_detail_api"),

    # blog app urls
    # path("posts/", views.PostList.as_view(), name="post_list_api"),
    # path("posts/<int:pk>/", views.PostDetail.as_view(), name="post_detail_api"),

    # path("users/", views.UserList.as_view(), name="user_list_api"),
    # path("users/<int:pk>/", views.UserDetail.as_view(), name="user_detail_api"),

]

urlpatterns += router.urls