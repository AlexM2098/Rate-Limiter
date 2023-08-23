from django.test import TestCase, Client

class RateLimiterTest(TestCase):
    def test_rate_limit(self):
        client = Client()
        # Make 6 requests rapidly
        for _ in range(6):
            response = client.get('/test/')
            if _ < 5:
                self.assertEqual(response.status_code, 200)
            else:
                self.assertEqual(response.status_code, 429)
