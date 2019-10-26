# Generated by Django 2.2.6 on 2019-10-26 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood_announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('announcement', models.TextField()),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Neighborhood')),
            ],
        ),
    ]
