# Generated by Django 3.0.6 on 2020-08-16 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0026_auto_20200816_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultadosexames',
            name='met3',
        ),
        migrations.RemoveField(
            model_name='resultadosexames',
            name='val3',
        ),
    ]