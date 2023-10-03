# Generated by Django 4.2.5 on 2023-10-02 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='idnp',
            field=models.PositiveIntegerField(default=0, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=13), django.core.validators.MaxLengthValidator(limit_value=13)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(),
        ),
    ]
