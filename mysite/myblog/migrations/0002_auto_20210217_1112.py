# Generated by Django 3.1.6 on 2021-02-17 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]