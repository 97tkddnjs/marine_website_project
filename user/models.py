from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta: #db table의 정보를 넣어주는 역할
        db_table = "my_user"


