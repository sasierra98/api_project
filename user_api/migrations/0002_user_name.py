# Generated by Django 4.0.3 on 2022-03-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Name'),
        ),
    ]