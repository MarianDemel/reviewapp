# Generated by Django 4.2.20 on 2025-04-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hodnoceni', '0004_place_place_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='datum_upraveni',
        ),
        migrations.RemoveField(
            model_name='review',
            name='datum_vytvoreni',
        ),
    ]
