# Generated by Django 2.2.6 on 2019-10-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_neighborhood_announcement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='occupants_count',
        ),
    ]
