from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    password_2 = models.CharField(max_length=20)
    registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# def user():
#     return None