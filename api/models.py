from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    second_name = models.CharField(max_length=150, verbose_name='Отчество')
    image = models.ImageField(upload_to='avatar', max_length=10000)

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    