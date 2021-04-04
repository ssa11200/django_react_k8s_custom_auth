from rest_framework import routers
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .views import SignupViewSet, SigninView, CurrentUserView, SignoutView

# router = routers.DefaultRouter()
# router.register("signup", SignupViewSet, basename="signup")

urlpatterns = [
    path("signup/", csrf_exempt(SignupViewSet.as_view()), name="signup"),
    path("signin/", csrf_exempt(SigninView.as_view()), name="signin"),
    path("currentuser/", csrf_exempt(CurrentUserView.as_view()), name="currentUser"),
    path("signout/", csrf_exempt(SignoutView.as_view()), name="signout"),
]
