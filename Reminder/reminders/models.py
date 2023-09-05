from django.db import models

class Reminder(models.Model):
    text = models.CharField(max_length=255)
    date_time = models.DateTimeField()
