# Generated by Django 3.0.6 on 2020-05-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_majortransfer_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='isadmin',
            field=models.CharField(choices=[('1', '1'), ('0', '0')], default='0', max_length=2),
        ),
    ]
