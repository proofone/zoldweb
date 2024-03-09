from django.test import TestCase, Client
from entities.models import User, Community, OtherEntity, Location


class UserTest(TestCase):
    def test_create_user(self):
        u = User.objects.create(username="test1", password="test1", email="test1@example.com")
        self.assertIsInstance(u, User)
        self.assertTrue(hasattr(u, 'pk'))

    def test_register_correct(self):
        c = Client()
        response = c.post("/register/", {
            "username": "test2", 
            "password": "test2", 
            "email": "test2@example.com"
            })
        
        self.assertEqual(response.status_code, 200)

    def test_register_no_email(self):
        c = Client()
        response = c.post("/register/", {
            # "username": "test2", 
            "password": "test2", 
            "email": "test2@example.com"
            })
        
        self.assertEqual(response.status_code, 403)
        
