# Generated by Django 4.2 on 2023-05-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0004_alter_arbitros_foto_alter_directores_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='foto',
            field=models.ImageField(default='image', upload_to='equipos/'),
            preserve_default=False,
        ),
    ]
