# Generated by Django 3.0.4 on 2020-03-10 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200309_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='persona_ci',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Persona'),
            preserve_default=False,
        ),
    ]
