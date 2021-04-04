from bson.objectid import ObjectId

# from rest_framework.request import Request

from .utils import TokenManager
from .models import User
from .serializers import SignupSerializer
from .errors import NotAuthorizedError
from .types import Request

# TODO: error handling
def current_user(view_function):
    def decorator(request: Request, *args, **kwargs):

        if "jwt" in request.session:

            jw_token = request.session.get("jwt")

            # TODO: error handeling for invalid token
            user_id = TokenManager.decode_token(jw_token)["userId"]

            # TODO: error handeling for invalid objectId
            user = User.objects.filter(_id=ObjectId(user_id)).first()

            request.current_user = (
                SignupSerializer(instance=user).data if user is not None else None
            )

        else:
            request.current_user = None

        return view_function(request, *args, **kwargs)

    return decorator


def require_auth(view_function):
    def decorator(request, *args, **kwargs):

        if request.current_user is None:
            # TODO: custom errors
            raise NotAuthorizedError()

        return view_function(request, *args, **kwargs)

    return decorator
