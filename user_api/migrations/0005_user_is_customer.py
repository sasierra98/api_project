# Generated by Django 4.0.3 on 2022-04-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0004_alter_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name="It's a customer"),
        ),
    ]
