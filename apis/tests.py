from django.test import TestCase

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from todos.models import Todo

# Create your tests here.

# books app tests
class BookAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "title",
            subtitle = "subtitle",
            author = "author",
            isbn = "1234567890123"
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)


# todos app tests
class TodoAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "title",
            body = "body"
        )

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail_api", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
