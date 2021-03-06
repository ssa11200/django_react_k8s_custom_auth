import jwt
from django.contrib.auth.hashers import check_password
from rest_framework.views import exception_handler
from copy import deepcopy
from rest_framework.serializers import ReturnDict
from rest_framework.response import Response
from typing import List, Dict
from bson.objectid import ObjectId

from .models import User
from .serializers import SignupSerializer
from .errors import BadRequestError, NotAuthorizedError
from .types import CustomError
from core.env_config import EnvConfig
from core.settings import SECRET_KEY as secret


class TokenManager:
    @staticmethod
    def create_token(userId: str) -> str:
        payload = {"userId": userId}
        return jwt.encode(payload, secret, algorithm="HS256").decode("utf-8")

    # TODO: error handeling
    @staticmethod
    def decode_token(token: str) -> str:
        try:
            return jwt.decode(token, secret)
        except Exception as error:
            print("Invalid token:", error)
            raise NotAuthorizedError


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


# convert string id to mongo object id
def string_to_objectId(string_id: str) -> ObjectId:
    try:
        return ObjectId(string_id)
    except Exception as error:
        print("Invalid id:", error)
        raise BadRequestError("Invalid object id.")
