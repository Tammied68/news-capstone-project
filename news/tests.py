"""Unit tests for the News application REST API."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from news.models import APIClientSubscription, Article, Publisher


class SubscribedArticleAPITest(TestCase):
    """Test the subscribed articles API endpoint."""

    def setUp(self):
        """Create test users, publisher, article, and API client subscription."""
        User = get_user_model()

        self.journalist = User.objects.create_user(
            username="journalist_api",
            password="testpass123",
            role=User.Role.JOURNALIST,
        )

        self.publisher = Publisher.objects.create(
            name="API Test Publisher",
            description="Publisher used for API tests.",
            website="https://example.com",
        )

        self.article = Article.objects.create(
            title="API Test Article",
            summary="API test summary",
            content="API test content",
            author=self.journalist,
            publisher=self.publisher,
            approved=True,
        )

        self.subscription = APIClientSubscription.objects.create(
            client_name="test-client",
            api_key="test123",
        )
        self.subscription.subscribed_publishers.add(self.publisher)

        self.client = APIClient()
        self.url = "/api/subscribed-articles/"

    def test_missing_api_key_returns_unauthorized(self):
        """API should reject requests without an API key."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.data)

    def test_invalid_api_key_returns_unauthorized(self):
        """API should reject requests with an invalid API key."""
        response = self.client.get(
            self.url,
            HTTP_X_API_KEY="wrong-key",
        )

        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.data)

    def test_valid_api_key_returns_subscribed_articles(self):
        """API should return approved articles for subscribed publishers."""
        response = self.client.get(
            self.url,
            HTTP_X_API_KEY="test123",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "API Test Article")
        self.assertEqual(response.data[0]["publisher"], "API Test Publisher")
