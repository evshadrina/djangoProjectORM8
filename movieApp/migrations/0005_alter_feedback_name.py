# Generated by Django 4.2 on 2023-05-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0004_alter_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='Имя1', max_length=40),
        ),
    ]