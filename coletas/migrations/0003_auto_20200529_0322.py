# Generated by Django 3.0.6 on 2020-05-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0002_auto_20200529_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='alergias',
            field=models.ManyToManyField(null=True, to='coletas.Alergia'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='comorbidades',
            field=models.ManyToManyField(null=True, to='coletas.Comorbidade'),
        ),
    ]
