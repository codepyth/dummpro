# Generated by Django 4.0.2 on 2023-10-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_attachments_attachment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.AddField(
            model_name='registration',
            name='attachment1',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AddField(
            model_name='registration',
            name='attachment2',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AddField(
            model_name='registration',
            name='attachment3',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AddField(
            model_name='registration',
            name='attachment4',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
    ]