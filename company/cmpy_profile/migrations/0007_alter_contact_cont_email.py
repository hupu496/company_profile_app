# Generated by Django 3.2.4 on 2021-06-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmpy_profile', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cont_email',
            field=models.EmailField(max_length=254),
        ),
    ]
