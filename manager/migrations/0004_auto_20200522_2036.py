# Generated by Django 3.0.4 on 2020-05-22 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20200521_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major', to='manager.Campus'),
        ),
        migrations.AlterField(
            model_name='myclass',
            name='head_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HostClass', to='manager.Teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='myClass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='manager.myClass'),
        ),
        migrations.AlterField(
            model_name='validlesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ValidLesson', to='manager.Teacher'),
        ),
    ]
