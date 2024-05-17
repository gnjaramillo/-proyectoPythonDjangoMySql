# Generated by Django 5.0.4 on 2024-04-24 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('getNombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelCodigo', models.CharField(max_length=9)),
                ('pelTitulo', models.CharField(max_length=50)),
                ('pelProtagonista', models.CharField(max_length=50)),
                ('pelDuracion', models.IntegerField()),
                ('pelResumen', models.CharField(max_length=2000)),
                ('pelFoto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('pelGenero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPeliculas.genero')),
            ],
        ),
    ]
