# Generated by Django 3.0.6 on 2021-03-26 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coletas', '0045_auto_20210325_2048'),
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