# Generated by Django 3.0.6 on 2020-08-01 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0020_auto_20200801_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dias_sintoma',
            name='sintomas1',
        ),
        migrations.AddField(
            model_name='dias_sintoma',
            name='sintoma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coletas.Sintoma'),
        ),
    ]