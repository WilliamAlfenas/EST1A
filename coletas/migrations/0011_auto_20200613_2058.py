# Generated by Django 3.0.6 on 2020-06-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0010_auto_20200616_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='form_consentimento',
            field=models.FileField(blank=True, null=True, upload_to='consentimento/%Y/%m/%d/', verbose_name='Formulário de Consentimento'),
        ),
    ]