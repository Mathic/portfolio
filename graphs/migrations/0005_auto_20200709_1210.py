# Generated by Django 2.1 on 2020-07-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0004_testtable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='month',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='event',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
