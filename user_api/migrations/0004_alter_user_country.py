# Generated by Django 4.0.3 on 2022-03-30 05:44

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_alter_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='Country'),
        ),
    ]
