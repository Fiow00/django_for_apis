from django.shortcuts import render

from rest_framework import generics

from books.models import Book
from todos.models import Todo
from .serializers import BookSerializer, TodoSerializer

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
