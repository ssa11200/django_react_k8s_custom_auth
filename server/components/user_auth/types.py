from rest_framework import request
from rest_framework.serializers import ReturnDict
from typing import TypedDict, Union


class RequestUser(ReturnDict):
    _id: str
    name: str
    email: str


# augment request object
class Request(request.Request):
    current_user: Union[RequestUser, None]


class CustomError(TypedDict):
    message: str
