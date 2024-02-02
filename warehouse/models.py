from django.db import models


class Component(models.Model):
    code = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    characteristics = models.CharField(max_length=100)
    quantity = models.IntegerField

    class Meta:
        db_table = 'components'


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    email = models.EmailField()

    class Meta:
        db_table = 'users'


class UserComponentPivot(models.Model):
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'components_users_pivot'
