# Generated by Django 4.1.3 on 2022-11-30 18:54

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_admission_college_email_admission_phoneno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='phoneno',
            field=models.CharField(max_length=10, validators=[data.models.validiate_phone_no]),
        ),
    ]