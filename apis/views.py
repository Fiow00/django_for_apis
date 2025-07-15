from django.shortcuts import render

from rest_framework import generics, permissions

from books.models import Book
from todos.models import Todo
from posts.models import Post
from .serializers import BookSerializer, TodoSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

# books app views
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# todos app views
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# posts app views
class PostList(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
