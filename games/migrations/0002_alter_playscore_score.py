# Generated by Django 4.0.5 on 2022-06-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playscore',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
