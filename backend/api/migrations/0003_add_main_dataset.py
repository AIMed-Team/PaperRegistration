# Generated by Django 3.1.3 on 2021-05-22 21:06

from django.db import migrations, models


def forwards(apps, schema_editor):
    Dataset = apps.get_model('api', 'Dataset')
    Dataset.objects.create(name='Main')


def rollback(apps, schema_editor):
    Dataset = apps.get_model('api', 'Dataset')
    Dataset.objects.filter(name='Main').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_metric_paper'),
    ]

    operations = [
        migrations.RunPython(forwards, rollback),
    ]