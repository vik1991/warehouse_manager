from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    code = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    characteristics = models.CharField(max_length=100)
    quantity = models.IntegerField

    class Meta:
        db_table = 'components'


class UserComponentPivot(models.Model):
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'components_users_pivot'
