from rest_framework.test import APITestCase
from rest_framework import status
from copy import deepcopy
import random_object_id

from .test_helpers import signin_user_with_session
from ..utils import omit
from ..models import User


class SignupTestCases(APITestCase):
    url = "/api/users/signup/"
    payload = {"email": "test@gmail.com", "password": "password", "name": "sadegh"}

    def test_signup_valid_email(self):
        payload = {**self.payload, "email": "wrong_email"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_password_length(self):
        payload = {**self.payload, "password": "1234"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_extra_field(self):
        payload = {**self.payload, "field": "value"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_missing_field(self):
        for key in self.payload:
            omitted_payload = omit(self.payload, key)
            response = self.client.post(self.url, omitted_payload)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_disallow_duplicate_email(self):
        payload = self.payload

        # first signup
        self.client.post(self.url, payload)

        # second signup with the same email
        response = self.client.post(self.url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_successful_signup(self):
        payload = self.payload
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(self.client.session.get("jwt"))


class SigninTestCases(APITestCase):
    url = "/api/users/signin/"
    payload = {"email": "test@gmail.com", "password": "password"}

    def test_signin_valid_email(self):
        payload = {**self.payload, "email": "wrong_email"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_password_length(self):
        payload = {**self.payload, "password": "1234"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_missing_field(self):
        for key in self.payload:
            omitted_payload = omit(self.payload, key)
            response = self.client.post(self.url, omitted_payload)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_extra_field(self):
        payload = {**self.payload, "field": "value"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_not_registered_user(self):
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_wrong_password(self):
        user = User.objects.create(**{**self.payload, "name": "sadegh"})
        response = self.client.post(self.url, {**self.payload, "password": "wrong"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_successful_signin(self):
        # first create the user in db
        user = User.objects.create(**{**self.payload, "name": "sadegh"})

        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(self.client.session.get("jwt"))

        # TODO: find a better way to compare db value with returned from api
        self.assertEqual(
            response.data,
            {"_id": str(user._id), "name": user.name, "email": user.email},
        )


class SignoutTestCases(APITestCase):
    url = "/api/users/signout/"
    user_payload = {"email": "test@gmail.com", "password": "password", "name": "sadegh"}

    def test_signout_user_not_loggedin(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_signout_success(self):
        # 1-create the use in db
        user = User.objects.create(**self.user_payload)

        # 2- signin user with session
        signin_user_with_session(str(user._id), self.client)

        # 3- signout the user
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})

        # check if jwt is deleted from session
        self.assertIsNone(self.client.session.get("jwt"))


class CurrentUserTestCases(APITestCase):
    url = "/api/users/currentuser/"
    user_payload = {"email": "test@gmail.com", "password": "password", "name": "sadegh"}

    def test_current_user_not_loggedin(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"currentUser": None})

    def test_current_user_doesnot_exists(self):
        # sign in a random user id which does not exists in db
        random_id = random_object_id.generate()
        signin_user_with_session(random_id, self.client)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"currentUser": None})

    def test_current_user_success(self):
        # 1-create the use in db
        user = User.objects.create(**self.user_payload)

        # 2- signin user with session
        signin_user_with_session(str(user._id), self.client)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # TODO: find a better way to compare db value with returned from api
        self.assertEqual(
            response.data,
            {
                "currentUser": {
                    "_id": str(user._id),
                    "name": user.name,
                    "email": user.email,
                }
            },
        )
