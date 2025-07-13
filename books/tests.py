from django.test import TestCase

from django.urls import reverse

from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "title",
            subtitle = "subtitle",
            author = "author",
            isbn = "1234567890123"
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "title")
        self.assertEqual(self.book.subtitle, "subtitle")
        self.assertEqual(self.book.author, "author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertContains(response, "subtitle")
