# Generated by Django 4.1.3 on 2022-11-30 18:47

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='college_email',
            field=models.EmailField(default='nt@sggs.ac.in', max_length=25, validators=[data.models.validiate_college_email]),
        ),
        
        migrations.AlterField(
            model_name='student',
            name='Photo',
            field=models.ImageField(upload_to='myimage'),
        ),
    ]
