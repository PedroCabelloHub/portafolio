# Generated by Django 4.2 on 2023-05-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_alter_arbitros_foto_alter_directores_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbitros',
            name='foto',
            field=models.ImageField(upload_to='arbitros/'),
        ),
        migrations.AlterField(
            model_name='directores',
            name='foto',
            field=models.ImageField(upload_to='directores/'),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='foto',
            field=models.ImageField(upload_to='jugadores/'),
        ),
        migrations.AlterField(
            model_name='ligas',
            name='foto',
            field=models.ImageField(upload_to='ligas/'),
        ),
    ]