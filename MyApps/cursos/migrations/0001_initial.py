# Generated by Django 5.1.2 on 2024-11-02 00:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la asignatura', max_length=30)),
                ('descripcion', models.TextField(help_text='Descripción de la asignatura', max_length=250)),
                ('creditos', models.IntegerField(help_text='Créditos de la asignatura', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('codigo', models.IntegerField(help_text='Código de la asignatura')),
            ],
            options={
                'verbose_name': 'asignatura',
                'verbose_name_plural': 'asignaturas',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Título del tema', max_length=30)),
                ('descripcion', models.TextField(help_text='Descripción del tema', max_length=250)),
                ('recor', models.FileField(help_text='Prueba', upload_to='')),
                ('asignatura', models.ForeignKey(help_text='Asignatura del tema', on_delete=django.db.models.deletion.CASCADE, to='cursos.asignatura')),
            ],
            options={
                'verbose_name': 'tema',
                'verbose_name_plural': 'temas',
            },
        ),
    ]