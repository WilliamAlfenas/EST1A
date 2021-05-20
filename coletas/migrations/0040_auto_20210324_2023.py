# Generated by Django 3.0.6 on 2021-03-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0039_auto_20210324_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='medicacao_diaria2',
            field=models.ManyToManyField(blank=True, null=True, to='coletas.Medicacao_Diaria', verbose_name='Medicação Diária'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tempo_rec',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tempo de Recuperação (dias)'),
        ),
    ]
