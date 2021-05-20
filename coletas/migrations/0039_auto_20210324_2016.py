# Generated by Django 3.0.6 on 2021-03-24 23:16

import coletas.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0038_auto_20210324_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicacao_Diaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=400, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Medicação Diária',
                'verbose_name_plural': 'Medicações diárias',
            },
            bases=(coletas.models.AutoDesc, models.Model),
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='medicacao_diaria',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cidade_nasc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cidade_nasc', to='coletas.Cidade', verbose_name='Cidade de Nascimento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dt_nasc',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='idade',
            field=models.IntegerField(blank=True, verbose_name='Idade'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='medicacao_diaria2',
            field=models.ManyToManyField(blank=True, null=True, to='coletas.Medicacao_Diaria'),
        ),
    ]
