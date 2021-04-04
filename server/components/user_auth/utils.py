import jwt
from django.contrib.auth.hashers import check_password
from rest_framework.views import exception_handler
from copy import deepcopy
from rest_framework.serializers import ReturnDict
from rest_framework.response import Response
from typing import List, Dict

from .models import User
from .serializers import SignupSerializer
from .errors import BadRequestError
from .types import CustomError


class TokenManager:
    @staticmethod
    # TODO: replace secret
    def create_token(userId: str) -> str:
        return jwt.encode({"userId": userId}, "secret", algorithm="HS256").decode(
            "utf-8"
        )

    # TODO: error handeling
    @staticmethod
    def decode_token(token: str) -> str:
        return jwt.decode(token, "secret")


# TODO: move to a proper module
def authenticate(email: str, password: str) -> ReturnDict:

    user = User.objects.filter(email=email).first()

    if user is None:
        raise BadRequestError("Invalid credentials.")

    passwords_match = check_password(password, user.password)

    if not passwords_match:
        raise BadRequestError("Invalid credentials.")

    return SignupSerializer(instance=user).data


# to be in agreement with frontend error handling
# TODO: frontend error handling was originally designed for express js and ajv body validator, redesign it for DRF serilizers
def custom_exception_handler(exc, context) -> Response:
    # original DRF exception handeler
    response = exception_handler(exc, context)

    errors: List[CustomError] = []

    # format the response as per frontend error handling
    if response and response.data:
        for error in response.data:
            for message in response.data[error]:
                errors.append({"message": "{}: {}".format(error, message)})

        response.data = {"errors": errors}

    return response


def omit(dictionary: dict, key: str) -> dict:
    omitted_dict = deepcopy(dictionary)
    del omitted_dict[key]
    return omitted_dict