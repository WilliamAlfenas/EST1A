# Generated by Django 3.0.6 on 2020-07-24 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0013_auto_20200629_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='sintomas01',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma01', to='coletas.Sintoma', verbose_name='Sintomas - dia 01'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas02',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma02', to='coletas.Sintoma', verbose_name='Sintomas - dia 02'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas03',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma03', to='coletas.Sintoma', verbose_name='Sintomas - dia 03'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas04',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma04', to='coletas.Sintoma', verbose_name='Sintomas - dia 04'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas05',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma05', to='coletas.Sintoma', verbose_name='Sintomas - dia 05'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas06',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma06', to='coletas.Sintoma', verbose_name='Sintomas - dia 06'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas07',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma07', to='coletas.Sintoma', verbose_name='Sintomas - dia 07'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas08',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma08', to='coletas.Sintoma', verbose_name='Sintomas - dia 08'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas09',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma09', to='coletas.Sintoma', verbose_name='Sintomas - dia 09'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas10',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma10', to='coletas.Sintoma', verbose_name='Sintomas - dia 10'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas11',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma11', to='coletas.Sintoma', verbose_name='Sintomas - dia 11'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas12',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma12', to='coletas.Sintoma', verbose_name='Sintomas - dia 12'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas13',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma13', to='coletas.Sintoma', verbose_name='Sintomas - dia 13'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas14',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma14', to='coletas.Sintoma', verbose_name='Sintomas - dia 14'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sintomas15',
            field=models.ManyToManyField(blank=True, null=True, related_name='Sintoma15', to='coletas.Sintoma', verbose_name='Sintomas - dia 15'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coletas.Origem', verbose_name='Indicação'),
        ),
    ]
