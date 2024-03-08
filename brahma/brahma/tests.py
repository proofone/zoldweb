from django.test import TestCase, Client


class BasicTest(TestCase):
    def test_home_page(self):
        c = Client()
        response = c.get("/")
        
        self.assertEqual(response.status_code, 200)

