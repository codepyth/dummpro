# Generated by Django 4.2.6 on 2023-10-29 18:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_alter_category_a_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_a',
            name='user',
        ),
        migrations.AddField(
            model_name='category_a',
            name='user',
            field=models.ManyToManyField(related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
