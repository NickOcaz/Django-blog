# Generated by Django 4.2.17 on 2025-01-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='updated_on',
            new_name='last_updated',
        ),
    ]
