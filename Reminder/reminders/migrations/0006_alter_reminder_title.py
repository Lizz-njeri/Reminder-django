# Generated by Django 4.2.5 on 2023-09-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0005_alter_reminder_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]