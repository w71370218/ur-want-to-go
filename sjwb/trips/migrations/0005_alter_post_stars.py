# Generated by Django 4.1 on 2022-09-14 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_post_lat_post_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stars',
            field=models.IntegerField(default=1, help_text='<font color="red">*必填</font>', max_length=1, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
