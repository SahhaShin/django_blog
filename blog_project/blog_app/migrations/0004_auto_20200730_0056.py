# Generated by Django 3.0.7 on 2020-07-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20200730_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='selectType',
            field=models.CharField(max_length=20),
        ),
    ]
