# models.py

from django.db import models
import datetime

class Reminder(models.Model):
    title = models.CharField(max_length=100, default='')
    date = models.DateField(default='2023-09-08')
    time = models.TimeField()
    phone_number = models.CharField(max_length=15, default='254714805460')  # For storing the recipient's phone number

    def __str__(self):
        return self.title
