# Generated by Django 4.0.2 on 2023-10-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_registration_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='visa_status',
            field=models.CharField(blank=True, choices=[('Permit', 'Permit'), ('Visit_Visa', 'Visit Visa'), ('Temporary_Permit', 'Temporary Permit'), ('Other', 'Other')], max_length=20, null=True),
        ),
    ]
