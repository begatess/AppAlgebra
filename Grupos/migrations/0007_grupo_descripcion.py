# Generated by Django 4.2.1 on 2023-10-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupos', '0006_alter_grupo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='descripcion',
            field=models.CharField(default='Sin descripción', max_length=400),
        ),
    ]
