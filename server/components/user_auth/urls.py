from django.urls import path

from .views import SignupViewSet, SigninView, CurrentUserView, SignoutView

urlpatterns = [
    path("signup/", SignupViewSet.as_view(), name="signup"),
    path("signin/", SigninView.as_view(), name="signin"),
    path("currentuser/", CurrentUserView.as_view(), name="currentUser"),
    path("signout/", SignoutView.as_view(), name="signout"),
]
