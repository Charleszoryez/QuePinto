# Generated by Django 3.0.4 on 2020-03-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nameEvent',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
