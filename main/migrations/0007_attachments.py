# Generated by Django 4.0.2 on 2023-10-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_registration_visa_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment1', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('attachment2', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('attachment3', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('attachment4', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
    ]