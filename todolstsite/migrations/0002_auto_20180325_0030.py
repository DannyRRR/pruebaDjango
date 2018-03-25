# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolstsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(to='todolstsite.Usuario'),
        ),
    ]
