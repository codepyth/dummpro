# Generated by Django 4.0.2 on 2023-10-24 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_attachments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attachments',
            new_name='Attachment',
        ),
    ]
