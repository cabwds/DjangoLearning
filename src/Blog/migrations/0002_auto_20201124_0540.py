# Generated by Django 3.1.3 on 2020-11-24 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='contetn',
            new_name='content',
        ),
    ]