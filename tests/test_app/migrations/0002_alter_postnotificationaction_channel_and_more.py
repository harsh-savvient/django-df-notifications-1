# Generated by Django 4.1.5 on 2023-01-12 08:50

import df_notifications.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnotificationaction',
            name='channel',
            field=df_notifications.fields.NoMigrationsChoicesField(max_length=255),
        ),
        migrations.AlterField(
            model_name='postnotificationreminder',
            name='channel',
            field=df_notifications.fields.NoMigrationsChoicesField(max_length=255),
        ),
    ]