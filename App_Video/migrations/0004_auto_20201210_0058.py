# Generated by Django 3.1.4 on 2020-12-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Video', '0003_auto_20201209_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=120),
        ),
    ]