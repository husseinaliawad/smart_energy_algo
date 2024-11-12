# Generated by Django 5.1.2 on 2024-11-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_power', models.FloatField()),
                ('min_power', models.FloatField()),
                ('current_power', models.FloatField(default=0)),
            ],
        ),
    ]