from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    picture = models.ImageField()

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()

    def __str__(self):
        return str(self.total)