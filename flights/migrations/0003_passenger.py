# Generated by Django 3.2 on 2021-06-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210608_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]