# Generated by Django 3.0.6 on 2020-05-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200520_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validlesson',
            name='begin_time',
            field=models.CharField(choices=[('MONDAY1', 'Monday1'), ('Monday2', 'Monday2'), ('Monday3', 'Monday3'), ('Monday4', 'Monday4'), ('Monday5', 'Monday5'), ('Monday6', 'Monday6'), ('Monday7', 'Monday7'), ('Monday8', 'Monday8'), ('Monday9', 'Monday9'), ('Tuesday1', 'Tuesday1'), ('Tuesday2', 'Tuesday2'), ('Tuesday3', 'Tuesday3'), ('Tuesday4', 'Tuesday4'), ('Tuesday5', 'Tuesday5'), ('Tuesday6', 'Tuesday6'), ('Tuesday7', 'Tuesday7'), ('Tuesday8', 'Tuesday8'), ('Tuesday9', 'Tuesday9'), ('Wednesday1', 'Wednesday1'), ('Wednesday2', 'Wednesday2'), ('Wednesday3', 'Wednesday3'), ('Wednesday4', 'Wednesday4'), ('Wednesday5', 'Wednesday5'), ('Wednesday6', 'Wednesday6'), ('Wednesday7', 'Wednesday7'), ('Wednesday8', 'Wednesday8'), ('Wednesday9', 'Wednesday9'), ('Thursday1', 'Thursday1'), ('Thursday2', 'Thursday2'), ('Thursday3', 'Thursday3'), ('Thursday4', 'Thursday4'), ('Thursday5', 'Thursday5'), ('Thursday6', 'Thursday6'), ('Thursday7', 'Thursday7'), ('Thursday8', 'Thursday8'), ('Thursday9', 'Thursday9'), ('Friday1', 'Friday1'), ('Friday2', 'Friday2'), ('Friday3', 'Friday3'), ('Friday4', 'Friday4'), ('Friday5', 'Friday5'), ('Friday6', 'Friday6'), ('Friday7', 'Friday7'), ('Friday8', 'Friday8'), ('Friday9', 'Friday9')], max_length=30),
        ),
    ]
