from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField('이름', max_length=30)
    team_name = models.CharField('소속 팀', max_length=30)
