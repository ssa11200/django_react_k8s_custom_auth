from rest_framework.test import APITestCase

from ..models import User
from ..serializers import SignupSerializer
from django.test import TestCase


class SignupSerializerTestCases(TestCase):
    def setUp(self):
        self.user_arrtibute = {
            "name": "sadegh",
            "password": "password",
            "email": "test@gmail.com",
        }

        self.user = User.objects.create(**self.user_arrtibute)
        self.serializer = SignupSerializer(instance=self.user)

    def test_returns_expected_data(self):
        data = self.serializer.data

        # we expect serializer does not to return password for security reasons
        self.assertTrue("password" not in data)
