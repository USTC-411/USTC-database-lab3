# Generated by Django 3.0.4 on 2020-05-23 03:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_majortransfer_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonselect',
            name='score',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]