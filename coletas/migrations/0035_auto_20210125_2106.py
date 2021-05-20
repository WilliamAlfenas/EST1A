# Generated by Django 3.0.6 on 2021-01-26 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0034_auto_20210110_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='tomou_antes',
        ),
        migrations.AddField(
            model_name='paciente',
            name='tipo_paciente',
            field=models.CharField(choices=[('Profilaxia', 'Profilaxia'), ('Assintomático', 'Assintomático'), ('Sintomático', 'Sintomático')], default='Profilaxia', max_length=128, verbose_name='Tipo de Paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='tomou_antes_ch',
            field=models.CharField(choices=[('Sim, tomou ANTES de iniciar o Tratamento', 'Sim, tomou ANTES de iniciar o Tratamento'), ('Sim, tomou APÓS iniciar o Tratamento', 'Sim, tomou APÓS iniciar o Tratamento'), ('Não', 'Não')], default='Não', max_length=128, verbose_name='Tomou Medicações em Estudo antes do tratamento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coletas.Cidade', verbose_name='Residência atual'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='met1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m1', to='coletas.MetricasExame'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='met2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m2', to='coletas.MetricasExame'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='met3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m3', to='coletas.MetricasExame'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='val1',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='val2',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='resultadosexames',
            name='val3',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor'),
        ),
    ]