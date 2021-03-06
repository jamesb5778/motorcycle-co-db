# Generated by Django 3.2.9 on 2021-11-17 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_motorcycle_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle_model',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='motorcycle_model', to='main_app.motorcycle_company'),
        ),
        migrations.AlterField(
            model_name='motorcycle_model',
            name='Specs',
            field=models.TextField(max_length=500),
        ),
    ]
