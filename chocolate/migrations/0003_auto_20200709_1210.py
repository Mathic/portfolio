# Generated by Django 2.1 on 2020-07-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolate', '0002_auto_20200615_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolatebar',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]