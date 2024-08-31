from django.db import models
from django.contrib.auth import get_user_model


class Resource(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='resources')


class UserResource(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='resources'
    )
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(verbose_name='Количество')


class UniqueItem(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='unique')


class UserUniqueItem(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='unique'
    )
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(verbose_name='Количество')

"""
В дальнейшем можно добавить каждому предмету вес выпадения / ценности
Для алгоритма дропа предметов из всего пула
"""