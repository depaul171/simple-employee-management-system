from email.policy import default
from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):

    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('prefer not to say', 'PREFER NOT TO SAY'),
    )

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    address = models.TextField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
