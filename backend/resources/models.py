from django.db import models
from django.contrib.auth import get_user_model


class RawResources(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='raw_resources'
    )
    stone = models.PositiveIntegerField(default=0)
    iron = models.PositiveIntegerField(default=0)
    copper = models.PositiveIntegerField(default=0)
    quartz = models.PositiveIntegerField(default=0)
    amber = models.PositiveIntegerField(default=0)

    def remove_resource(self, resource_name, amount):
        current_value = getattr(self, resource_name)
        if current_value >= amount:
            setattr(self, resource_name, current_value - amount)
            self.save()
        else:
            raise ValueError("Not enough resources")


class ProcessedMaterials(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='processed_materials'
    )
    iron_ingot = models.PositiveIntegerField(default=0)
    copper_ingot = models.PositiveIntegerField(default=0)
    quartz_ingot = models.PositiveIntegerField(default=0)
    amber_ingot = models.PositiveIntegerField(default=0)

    def add_resource(self, resource_name, amount):
        current_value = getattr(self, resource_name)
        setattr(self, resource_name, current_value + amount)
        self.save()


# class UniqueItem(models.Model):
#     name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    # предмет должен давать какие-то преимущества, как вариант можно вьебать мультипликатор просто


class ResourceManager:
    def __init__(self, user):
        self.user = user
        self.raw_resources = user.raw_resources
        self.processed_materials = user.processed_materials

    def process_iron(self):
        if self.raw_resources.iron >= 10:
            self.raw_resources.remove_resource('iron', 10)
            self.processed_materials.add_resource('iron_ingot', 1)
        else:
            raise ValueError("Not enough iron to process")

    def process_copper(self):
        if self.raw_resources.copper >= 10:
            self.raw_resources.remove_resource('copper', 10)
            self.processed_materials.add_resource('copper_ingot', 1)
        else:
            raise ValueError("Not enough copper to process")
