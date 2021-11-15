# Generated by Django 3.2.9 on 2021-11-15 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycle_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('year_created', models.CharField(max_length=4)),
                ('Specs', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
