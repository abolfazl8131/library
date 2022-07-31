from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rest_framework.test import APITestCase

# class to define a test case for SignUp

class UserSignUpTestCase(APITestCase):
    # some setup here, explained later

    def test_correct_signUp(self):
       pass

    def test_if_password_incorrect_then_cant_login(self):
       pass

    def test_if_user_not_registered_cant_login(self):
        pass
