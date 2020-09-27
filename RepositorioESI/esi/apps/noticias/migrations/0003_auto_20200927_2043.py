# Generated by Django 3.0 on 2020-09-27 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20200926_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='autor',
            field=models.CharField(max_length=200, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='new',
            name='copete',
            field=models.TextField(verbose_name='copete'),
        ),
        migrations.AlterField(
            model_name='new',
            name='cuerpo',
            field=models.TextField(verbose_name='texo'),
        ),
        migrations.AlterField(
            model_name='new',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de la publicacion'),
        ),
        migrations.AlterField(
            model_name='new',
            name='fuente',
            field=models.URLField(max_length=400, verbose_name='fuente URL'),
        ),
        migrations.AlterField(
            model_name='new',
            name='imagen',
            field=models.ImageField(upload_to='', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='new',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='titulo de la noticia'),
        ),
    ]
