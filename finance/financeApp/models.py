from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    lastIncome = models.DecimalField(decimal_places=2, max_digits=10)
    lastOutcome = models.DecimalField(decimal_places=2, max_digits=10)
