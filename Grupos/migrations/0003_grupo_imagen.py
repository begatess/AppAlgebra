# Generated by Django 4.2.1 on 2023-06-27 00:25

import Grupos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupos', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='imagen',
            field=models.ImageField(blank=True, default=Grupos.models.default_imagen, null=True, upload_to='media/img_porfile'),
        ),
    ]
