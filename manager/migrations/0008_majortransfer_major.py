# Generated by Django 3.0.4 on 2020-05-22 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20200522_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='majortransfer',
            name='major',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='major_transfer', to='manager.Major'),
        ),
    ]
