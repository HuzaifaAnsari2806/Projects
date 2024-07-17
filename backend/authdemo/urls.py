from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import (
    LoginFormView,
    logout_user,
    LoginView,
    RegisterView,
    LoginAuthenticationView
    )


urlpatterns = [
    path("", LoginFormView, name="login-form"),
    path("loginauth/", LoginAuthenticationView.as_view()),
    path("register/",RegisterView.as_view()),
    path("login/", LoginView.as_view(), name="login-api"),
    path("logout/", logout_user, name="log-out")
]
# urlpatterns += router.urls
