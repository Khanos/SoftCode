# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(max_length=30)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('cedula', models.IntegerField(default=0)),
                ('fecha_de_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('telefono_casa', models.IntegerField(default=0)),
                ('telefono_oficina', models.IntegerField(default=0)),
                ('telefono_celular', models.IntegerField(default=0)),
                ('correo', models.EmailField(max_length=75)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('direccion', models.TextField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
