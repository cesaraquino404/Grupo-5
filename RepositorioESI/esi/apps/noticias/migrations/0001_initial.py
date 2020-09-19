# Generated by Django 3.0 on 2020-09-16 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
