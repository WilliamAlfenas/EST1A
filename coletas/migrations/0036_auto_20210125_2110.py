# Generated by Django 3.0.6 on 2021-01-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0035_auto_20210125_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='tratamentos',
            field=models.ManyToManyField(null=True, to='coletas.Forma_Tratamento', verbose_name='Posologia'),
        ),
    ]
