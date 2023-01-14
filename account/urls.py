from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import AuthorRegisterView

urlpatterns = [
    path('api/account/register/', AuthorRegisterView.as_view()),
    # path('token/', obtain_auth_token),
]