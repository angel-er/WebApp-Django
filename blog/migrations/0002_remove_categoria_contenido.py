# Generated by Django 4.0.4 on 2022-05-30 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='contenido',
        ),
    ]