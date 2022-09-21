from django.test import TestCase

# Create your tests here
class MyWatchlistTest(TestCase):
    def test_html(self):
        response = self.client.get('/mywatchlist/html', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        response = self.client.get('/mywatchlist/xml', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = self.client.get('/mywatchlist/json', follow=True)
        self.assertEqual(response.status_code, 200)