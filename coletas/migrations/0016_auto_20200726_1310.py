# Generated by Django 3.0.6 on 2020-07-26 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0015_dias_sintoma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dias_sintoma',
            options={'verbose_name': 'Sintomas por dias', 'verbose_name_plural': 'Sintomas por dia'},
        ),
    ]
