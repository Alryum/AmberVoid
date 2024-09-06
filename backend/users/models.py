from typing import List, Dict
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.transaction import atomic
from .managers import CustomUserManager



class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=20, unique=True, verbose_name='Ник')
    email = models.EmailField(unique=True, verbose_name='Почта')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.nickname
    # TODO: Переделать запросы в базу через prefetch related
    def decrease_resources(self, query: List[Dict[str, int]]):      
        data = query.get('resources')
        with atomic.transaction():
            for item_name, quantity in data.items():
                user_resource = self.resources.get(resource__name=item_name)
                user_resource.decrease_quantity(quantity)
            
    def get_loot_multipliers(self):
        user_items = self.unique_items
        multipliers = 1
        for item in user_items:
            for counter in range(item.quantity):
                multipliers *= item.loot_multiplier
        return multipliers

