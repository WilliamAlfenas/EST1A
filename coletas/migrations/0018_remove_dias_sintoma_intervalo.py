# Generated by Django 3.0.6 on 2020-07-26 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0017_auto_20200726_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dias_sintoma',
            name='intervalo',
        ),
    ]