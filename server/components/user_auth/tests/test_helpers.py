from ..models import User
from ..utils import TokenManager
from ..serializers import SignupSerializer
from django.core import signing
from django.conf import settings as django_settings
from django.test import TestCase
from django.test import Client


def signin_user_with_session(user_id: str, client: Client):
    jw_token = TokenManager.create_token(user_id)

    session = client.session
    session["jwt"] = jw_token
    session.save()
    session_cookie = django_settings.SESSION_COOKIE_NAME
    client.cookies[session_cookie] = session.session_key
    cookie_data = {
        "max-age": None,
        "path": "/",
        "domain": django_settings.SESSION_COOKIE_DOMAIN,
        "secure": django_settings.SESSION_COOKIE_SECURE or None,
        "expires": None,
    }

    client.cookies[session_cookie].update(cookie_data)
