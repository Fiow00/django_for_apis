from django.test import TestCase

from .models import Todo


# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "title",
            body = "body"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "title")
        self.assertEqual(self.todo.body, "body")
        self.assertEqual(str(self.todo), "title")
