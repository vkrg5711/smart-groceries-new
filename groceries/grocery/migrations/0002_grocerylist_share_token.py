# Generated by Django 5.1.7 on 2025-03-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocerylist',
            name='share_token',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
