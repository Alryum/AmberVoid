
from django.urls import reverse
import pytest
from django.core.management import call_command
from resources.models import Resource
from users.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestUser:
    @pytest.fixture
    def users_fixture(self) -> None:
        call_command('loaddata', 'fixtures/v1.json', verbosity=0)

    def test_increment_with_correct_value(self, users_fixture):
        resources_dict = {'Resource 1': 10}
        user_1 = User.objects.get(pk=1)
        user_1.decrease_resources(resources_dict)
        resource_after_decrease = user_1.resources.get(resource__name='Resource 1').quantity
        assert resource_after_decrease == 90

    def test_increment_with_negative_value(self, users_fixture):
        resources_dict = {'Resource 1': -10}
        user_1 = User.objects.get(pk=1)
        with pytest.raises(ValidationError, match='Ожидается положительное число'):
            user_1.decrease_resources(resources_dict)
        resource_after_decrease = user_1.resources.get(resource__name='Resource 1').quantity
        assert resource_after_decrease == 100

    def test_increment_with_invalid_value(self, users_fixture):
        resources_dict = {'Resource 1': 200}
        user_1 = User.objects.get(pk=1)
        with pytest.raises(ValidationError, match='Недостаточное количество ресурса'):
            user_1.decrease_resources(resources_dict)
        resource_after_decrease = user_1.resources.get(resource__name='Resource 1').quantity
        assert resource_after_decrease == 100
