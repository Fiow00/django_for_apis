from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Post

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "user",
            email = "user@email.com",
            password = "secret",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "title",
            body = "body"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "user")
        self.assertEqual(self.post.title, "title")
        self.assertEqual(self.post.body, "body")
        self.assertEqual(str(self.post), "title")