import shutil
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.utils import timezone

from .models import Article, Comment

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ArticleViewsTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_like_article_increments_and_redirects(self):
        article = Article.objects.create(
            title='Test title',
            body='Test body',
            pub_date=timezone.now(),
            thumbnail=SimpleUploadedFile('thumb.jpg', b'test'),
        )

        response = self.client.get(f'/articles/like/{article.id}/')

        article.refresh_from_db()
        self.assertEqual(article.likes, 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], f'/articles/get/{article.id}')

    def test_add_comment_creates_comment_and_redirects(self):
        article = Article.objects.create(
            title='Test title',
            body='Test body',
            pub_date=timezone.now(),
            thumbnail=SimpleUploadedFile('thumb.jpg', b'test'),
        )

        response = self.client.post(
            f'/articles/add_comment/{article.id}/',
            data={'name': 'Alice', 'body': 'Nice post!'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], f'/articles/get/{article.id}')
        self.assertEqual(Comment.objects.filter(article=article).count(), 1)
        comment = Comment.objects.get(article=article)
        self.assertEqual(comment.name, 'Alice')
        self.assertEqual(comment.body, 'Nice post!')
        self.assertIsNotNone(comment.pub_date)
