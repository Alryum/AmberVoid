from django.db import models
from django.contrib.auth import get_user_model


class Resource(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='resources')

    def __str__(self) -> str:
        return self.name


class UserResource(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='resources'
    )
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(verbose_name='Количество')

    class Meta:
        unique_together = ('user', 'resource')


class UniqueItem(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='unique')

    def __str__(self) -> str:
        return self.name


class UserUniqueItem(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='unique_items'
    )
    unique_item = models.ForeignKey(UniqueItem, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(verbose_name='Количество')

    class Meta:
        unique_together = ('user', 'unique_item')


"""
В дальнейшем можно добавить каждому предмету вес выпадения / ценности
Для алгоритма дропа предметов из всего пула
"""
