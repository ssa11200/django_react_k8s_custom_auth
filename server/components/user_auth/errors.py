from rest_framework.exceptions import APIException
from rest_framework import status


class BadRequestError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail):
        super().__init__({"Error": [detail]})


class NotAuthorizedError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self):
        super().__init__({"Error": ["Not Authorized."]})


class NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self):
        super().__init__({"Error": ["Not Found."]})