# Generated by Django 4.1 on 2022-09-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_persona_alter_estudios_año_comienzo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='contacto',
            name='instagram',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='estudios',
            name='persona',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='persona',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='persona',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='proyecto',
            field=models.URLField(),
        ),
    ]
