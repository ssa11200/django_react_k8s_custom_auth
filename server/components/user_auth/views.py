from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator

from .serializers import SignupSerializer, SigninSerializer
from .utils import TokenManager, authenticate
from .decorators import current_user, require_auth
from .types import Request


class SignupViewSet(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request: Request, format=None) -> Response:
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        user = serializer.data

        jw_token = TokenManager.create_token(user["_id"])

        request.session["jwt"] = jw_token

        return Response(user, status=status.HTTP_201_CREATED)


class SigninView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SigninSerializer

    def post(self, request: Request, format=None) -> Response:

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.data)

        jw_token = TokenManager.create_token(user["_id"])
        request.session["jwt"] = jw_token

        return Response(user, status=status.HTTP_200_OK)


class CurrentUserView(APIView):
    @method_decorator(current_user)
    def get(self, request: Request, format=None) -> Response:

        return Response(
            {"currentUser": request.current_user}, status=status.HTTP_200_OK
        )


class SignoutView(APIView):
    @method_decorator(current_user)
    @method_decorator(require_auth)
    def post(self, request: Request, format=None) -> Response:
        del request.current_user
        del request.session["jwt"]
        return Response({}, status=status.HTTP_200_OK)
