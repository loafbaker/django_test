import shutil
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.utils import timezone

from .models import Article

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
